from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name
from .routes import register_routes

db = SQLAlchemy()


def create_app(env=None):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Location API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api)
    db.init_app(app)

    @app.route("/healthz")
    def health():
        return jsonify("OK - Healthy")

    return app
