from flask import Blueprint, jsonify, request

from app.services.bot_service import VCSMBotService

bot_bp = Blueprint("bot", __name__, url_prefix="/api/bot")


@bot_bp.route("/message", methods=["POST"])
def bot_message():
    payload = request.get_json(silent=True) or {}
    user_message = payload.get("message", "")
    reply = VCSMBotService.get_reply(user_message)
    return jsonify({"reply": reply})
