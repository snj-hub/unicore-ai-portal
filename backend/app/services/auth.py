from datetime import datetime, timedelta, timezone
import hashlib
import jwt
from flask import current_app


def hash_otp(otp: str):
    return hashlib.sha256(otp.encode()).hexdigest()


def create_token(student_id: int):
    now = datetime.now(timezone.utc)
    payload = {'sub': student_id, 'iat': int(now.timestamp()), 'exp': int((now + current_app.config['JWT_EXPIRES']).timestamp())}
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')


def decode_token(token: str):
    return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])


def otp_expiry():
    return datetime.utcnow() + timedelta(minutes=current_app.config['OTP_EXP_MINUTES'])
