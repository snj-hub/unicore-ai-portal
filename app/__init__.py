from flask import Flask

from app.config import Config
from app.routes.auth import auth_bp
from app.routes.bot import bot_bp
from app.routes.dashboard import dashboard_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(bot_bp)

    return app
