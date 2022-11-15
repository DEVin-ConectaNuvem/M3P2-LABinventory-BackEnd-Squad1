from flask import Flask
from flask_cors import CORS

from src.config import app_config


def create_app(environment):

    app = Flask(__name__)

    app.config.from_object(app_config[environment])
    CORS(app)
    app.config["Access-Control-Allow-Origin"] = "*"
    app.config["Access-Control-Allow-Headers"] = "Content-Type"

    return app
