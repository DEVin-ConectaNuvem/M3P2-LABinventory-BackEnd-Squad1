import os
import pytest
from src.app import create_app, mongo_client
from src.app.routes import routes
from flask import json

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

@pytest.fixture(scope="session")
def app():
    os.system("poetry run flask create_collections")
    
    app_on = create_app(os.getenv("FLASK_ENV"))
    routes(app_on)
    return app_on

  
@pytest.fixture
def create_user_in_client(client):
    data = {
        "email": "thiago@teste.com",
        "password": "12345678"
    }
    
    response = client.post("users/create", data=json.dumps(data), headers=headers)
    return response
  
  
@pytest.fixture
def logged_in_client(client):
    data = {
        "email": "teste@teste.com",
        "password": "12345678"
    }

    response = client.post("users/login", data=json.dumps(data), headers=headers)
    return response.json["token"]
