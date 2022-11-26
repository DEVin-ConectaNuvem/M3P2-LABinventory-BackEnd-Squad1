import json

from faker import Faker

mimetype = "application/json"
url = "/user/create"

headers = {"Content-Type": mimetype, "Accept": mimetype}

fake = Faker()


def test_login_user_successfully(client):
    data = {"email": fake.email(), "password": "12345678"}

    response = client.post("users/create", data=json.dumps(data), headers=headers)

    assert response.status_code == 201
    assert response.json["message"] == "Usuário foi criado com sucesso."

    response = client.post("users/login", data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json["token"], str)


def test_login_user_with_invalid_email(client):
    data = {"email": fake.email(), "password": "12345678"}

    response = client.post("users/login", data=json.dumps(data), headers=headers)

    assert response.status_code == 401
    assert response.json["error"] == "Suas credênciais estão incorretas!"
    assert response.json["status_code"] == 401


def test_login_user_with_invalid_password(client):
    data = {"email": fake.email(), "password": "12345678"}

    client.post("users/create", data=json.dumps(data), headers=headers)

    data["password"] = "senhainvalida"
    response = client.post("users/login", data=json.dumps(data), headers=headers)

    assert response.status_code == 401
    assert response.json["error"] == "Suas credênciais estão incorretas!"
    assert response.json["status_code"] == 401
