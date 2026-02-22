import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
    JWT_EXPIRES = timedelta(hours=int(os.getenv('JWT_EXPIRES_HOURS', '12')))
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root')
    MYSQL_DB = os.getenv('MYSQL_DB', 'unicore_ai')
    OTP_EXP_MINUTES = int(os.getenv('OTP_EXP_MINUTES', '5'))
    OTP_RATE_SECONDS = int(os.getenv('OTP_RATE_SECONDS', '60'))
    OTP_MAX_ATTEMPTS = int(os.getenv('OTP_MAX_ATTEMPTS', '5'))
    COLLEGE_DOMAIN = os.getenv('COLLEGE_DOMAIN', 'vcsm.ac.in')
