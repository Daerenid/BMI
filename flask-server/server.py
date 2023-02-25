from flask import Flask, jsonify
from models import db
from flask_migrate import Migrate
from routes import basic
import os
from typing import Optional


def get_env(name: str) -> Optional[str | int]:
    env = os.environ.get(name)
    if env is None:
        return None
    if env.isdigit():
        return int(env)
    return env


def setup_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BMI/app.sqlite3"
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)


def setup_routes(app: Flask) -> None:
    app.register_blueprint(basic.bp)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = get_env("SECRET_KEY")
    setup_database(app)
    setup_routes(app)
    app.run(debug=True)
    return app


if __name__ == "__main__":
    create_app()
