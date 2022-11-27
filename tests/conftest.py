import os

import pytest
from flask import json

from src.app import create_app, mongo_client
from src.app.routes import routes

mimetype = "application/json"
headers = {"Content-Type": mimetype, "Accept": mimetype}


@pytest.fixture(scope="session")
def app():
    os.system("poetry run flask create_collections")

    app_on = create_app("testing")
    routes(app_on)
    return app_on


@pytest.fixture
def logged_in_client(client):

    data = {"email": "admin@teste.com", "password": "12345678", "role": "ADMIN"}

    client.post("users/create", data=json.dumps(data), headers=headers)

    data = {"email": "admin@teste.com", "password": "12345678"}

    response = client.post("users/login", data=json.dumps(data), headers=headers)
    return response.json["token"]
