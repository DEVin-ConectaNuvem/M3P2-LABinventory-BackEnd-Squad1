import os
from flask import Flask
from src.app.config import app_config
from src.app.swagger import create_swagger
from flask_cors import CORS
from src.app.utils import mongo

def create_app(enviroment):
    global mongo_client
    
    app = Flask(__name__)
    app.config.from_object(app_config[enviroment])

    create_swagger(app)
    mongo.init_app(app)
    mongo_client = mongo.db

    CORS(app)
    
    return app
    
app = create_app(os.getenv("FLASK_ENV"))