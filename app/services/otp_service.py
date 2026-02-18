from datetime import datetime, timedelta
import random

from flask import session


class OTPService:
    OTP_SESSION_KEY = "login_otp"
    PHONE_SESSION_KEY = "login_phone"
    EXPIRES_AT_SESSION_KEY = "otp_expires_at"

    @staticmethod
    def generate_otp(phone_number: str) -> str:
        otp = str(random.randint(100000, 999999))
        expires_at = datetime.utcnow() + timedelta(minutes=5)

        session[OTPService.OTP_SESSION_KEY] = otp
        session[OTPService.PHONE_SESSION_KEY] = phone_number
        session[OTPService.EXPIRES_AT_SESSION_KEY] = expires_at.isoformat()

        return otp

    @staticmethod
    def verify_otp(phone_number: str, otp_input: str) -> bool:
        stored_otp = session.get(OTPService.OTP_SESSION_KEY)
        stored_phone = session.get(OTPService.PHONE_SESSION_KEY)
        expires_at_raw = session.get(OTPService.EXPIRES_AT_SESSION_KEY)

        if not stored_otp or not stored_phone or not expires_at_raw:
            return False

        expires_at = datetime.fromisoformat(expires_at_raw)
        is_not_expired = datetime.utcnow() <= expires_at
        is_valid = stored_phone == phone_number and stored_otp == otp_input and is_not_expired

        if is_valid:
            session.pop(OTPService.OTP_SESSION_KEY, None)
            session.pop(OTPService.EXPIRES_AT_SESSION_KEY, None)

        return is_valid
