from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for

from app.services.otp_service import OTPService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET", "POST"])
def login_request_otp():
    if request.method == "POST":
        phone_number = request.form.get("phone_number", "").strip()
        if not phone_number:
            flash("Please enter your registered mobile number.", "error")
            return redirect(url_for("auth.login_request_otp"))

        otp = OTPService.generate_otp(phone_number)
        if current_app.config["OTP_SIMULATION_MODE"]:
            flash(f"Simulated OTP (dev only): {otp}", "info")

        flash("OTP sent. Please verify to continue.", "success")
        return redirect(url_for("auth.verify_otp"))

    return render_template("login.html")


@auth_bp.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():
    if request.method == "POST":
        phone_number = request.form.get("phone_number", "").strip()
        otp_input = request.form.get("otp", "").strip()

        if OTPService.verify_otp(phone_number, otp_input):
            session["student_id"] = 1
            session["student_name"] = "Demo Student"
            flash("Login successful.", "success")
            return redirect(url_for("dashboard.student_dashboard"))

        flash("Invalid or expired OTP.", "error")

    return render_template("verify_otp.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login_request_otp"))
