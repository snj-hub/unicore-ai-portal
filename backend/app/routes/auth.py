from datetime import datetime
import random
from flask import Blueprint, jsonify, request, current_app
from ..db import get_conn
from ..services.auth import hash_otp, otp_expiry, create_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.post('/request-otp')
def request_otp():
    mobile = request.json.get('mobile', '').strip()
    if len(mobile) != 10 or not mobile.isdigit():
        return jsonify({'error': 'Invalid mobile'}), 400

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM otp_logins WHERE mobile=%s', (mobile,))
        row = cur.fetchone()
        if row and row.get('last_sent_at'):
            delta = (datetime.utcnow() - row['last_sent_at']).total_seconds()
            if delta < current_app.config['OTP_RATE_SECONDS']:
                return jsonify({'error': 'OTP requested too frequently'}), 429

        otp = ''.join(random.choices('0123456789', k=6))
        otp_h = hash_otp(otp)
        expires = otp_expiry()
        if row:
            cur.execute('UPDATE otp_logins SET otp_hash=%s, expires_at=%s, attempts=0, last_sent_at=UTC_TIMESTAMP() WHERE mobile=%s', (otp_h, expires, mobile))
        else:
            cur.execute('INSERT INTO otp_logins (mobile, otp_hash, expires_at, attempts, last_sent_at) VALUES (%s,%s,%s,0,UTC_TIMESTAMP())', (mobile, otp_h, expires))

    return jsonify({'message': 'OTP sent', 'debug_otp': otp})


@auth_bp.post('/verify-otp')
def verify_otp():
    mobile = request.json.get('mobile', '').strip()
    otp = request.json.get('otp', '').strip()
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM otp_logins WHERE mobile=%s', (mobile,))
        row = cur.fetchone()
        if not row:
            return jsonify({'error': 'No OTP request found'}), 404
        if row['attempts'] >= current_app.config['OTP_MAX_ATTEMPTS']:
            return jsonify({'error': 'Too many attempts'}), 429
        if row['expires_at'] < datetime.utcnow():
            return jsonify({'error': 'OTP expired'}), 400
        if hash_otp(otp) != row['otp_hash']:
            cur.execute('UPDATE otp_logins SET attempts=attempts+1 WHERE mobile=%s', (mobile,))
            return jsonify({'error': 'Invalid OTP'}), 401
        cur.execute('SELECT id, name, email, mobile FROM students WHERE mobile=%s', (mobile,))
        student = cur.fetchone()
        if not student:
            return jsonify({'error': 'Student not found'}), 404

    token = create_token(student['id'])
    return jsonify({'token': token, 'student': student})


@auth_bp.post('/google')
def google_login():
    email = request.json.get('email', '').strip().lower()
    domain = current_app.config['COLLEGE_DOMAIN']
    if not email.endswith(f'@{domain}'):
        return jsonify({'error': f'Use college email @{domain}'}), 400

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute('SELECT id, name, email, mobile FROM students WHERE email=%s', (email,))
        student = cur.fetchone()
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'token': create_token(student['id']), 'student': student})
