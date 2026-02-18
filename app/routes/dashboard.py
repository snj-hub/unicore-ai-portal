from flask import Blueprint, redirect, render_template, session, url_for

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
def student_dashboard():
    if not session.get("student_id"):
        return redirect(url_for("auth.login_request_otp"))

    student_data = {
        "name": session.get("student_name", "Student"),
        "pending_fees": "₹8,500",
        "attendance": "84%",
        "next_exam": "24 Oct 2026 - DBMS",
        "notices": [
            "Internal assessment starts next Monday.",
            "Lab record submission deadline: Friday 4 PM.",
        ],
    }

    return render_template("dashboard.html", student=student_data)
