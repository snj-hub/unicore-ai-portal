from datetime import date
from functools import wraps
import jwt
from flask import Blueprint, current_app, jsonify, request
from ..db import get_conn

api_bp = Blueprint('api', __name__)


def require_auth(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization', '')
        token = auth.replace('Bearer ', '')
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            request.student_id = payload['sub']
        except Exception:
            return jsonify({'error': 'Unauthorized'}), 401
        return fn(*args, **kwargs)
    return wrapper


@api_bp.get('/me')
@require_auth
def me():
    with get_conn().cursor() as cur:
        cur.execute('SELECT id,name,mobile,email,dept,year,section,roll_no FROM students WHERE id=%s', (request.student_id,))
        return jsonify(cur.fetchone())

@api_bp.get('/dashboard/summary')
@require_auth
def dashboard_summary():
    with get_conn().cursor() as cur:
        cur.execute('SELECT total_amount, paid_amount FROM fees WHERE student_id=%s', (request.student_id,))
        fees = cur.fetchone()
        cur.execute('SELECT COUNT(*) c FROM attendance WHERE student_id=%s', (request.student_id,))
        total = cur.fetchone()['c']
        cur.execute('SELECT COUNT(*) c FROM attendance WHERE student_id=%s AND present_bool=1', (request.student_id,))
        present = cur.fetchone()['c']
        return jsonify({'fees': fees, 'attendance_percent': round((present / total) * 100, 2) if total else 0})

@api_bp.get('/fees')
@require_auth
def fees():
    with get_conn().cursor() as cur:
        cur.execute('SELECT total_amount, paid_amount, last_payment_date FROM fees WHERE student_id=%s', (request.student_id,))
        row = cur.fetchone()
    row['remaining_amount'] = float(row['total_amount']) - float(row['paid_amount'])
    row['status'] = 'Paid' if row['remaining_amount'] <= 0 else 'Pending'
    return jsonify(row)

@api_bp.get('/attendance')
@require_auth
def attendance():
    with get_conn().cursor() as cur:
        cur.execute('SELECT date, subject, present_bool FROM attendance WHERE student_id=%s ORDER BY date DESC LIMIT 60', (request.student_id,))
        data = cur.fetchall()
    return jsonify(data)

@api_bp.get('/timetable/today')
@require_auth
def tt_today():
    day = date.today().strftime('%A')
    with get_conn().cursor() as cur:
        cur.execute('SELECT day_order FROM day_orders WHERE date=%s', (date.today(),))
        row = cur.fetchone()
        if row:
            cur.execute('SELECT period_no,start_time,end_time,subject,faculty FROM timetable WHERE day_order=%s ORDER BY period_no', (row['day_order'],))
        else:
            cur.execute('SELECT period_no,start_time,end_time,subject,faculty FROM timetable WHERE day_name=%s ORDER BY period_no', (day,))
        return jsonify(cur.fetchall())

@api_bp.get('/timetable/week')
@require_auth
def tt_week():
    with get_conn().cursor() as cur:
        cur.execute('SELECT day_name,period_no,start_time,end_time,subject,faculty FROM timetable ORDER BY FIELD(day_name, "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"), period_no')
        return jsonify(cur.fetchall())

@api_bp.get('/day-order/today')
@require_auth
def day_order():
    with get_conn().cursor() as cur:
        cur.execute('SELECT date, day_order FROM day_orders WHERE date=%s', (date.today(),))
        return jsonify(cur.fetchone() or {'date': str(date.today()), 'day_order': 'N/A'})

@api_bp.get('/exams/upcoming')
def exams():
    with get_conn().cursor() as cur:
        cur.execute('SELECT title,date,time,syllabus_link FROM exams WHERE date >= CURDATE() ORDER BY date LIMIT 10')
        return jsonify(cur.fetchall())

@api_bp.get('/events')
def events():
    with get_conn().cursor() as cur:
        cur.execute('SELECT title,date,category,description,is_past FROM events ORDER BY date DESC')
        return jsonify(cur.fetchall())

@api_bp.get('/placements/news')
def placements_news():
    with get_conn().cursor() as cur:
        cur.execute('SELECT title,date,content,tags FROM placement_news ORDER BY date DESC')
        return jsonify(cur.fetchall())
