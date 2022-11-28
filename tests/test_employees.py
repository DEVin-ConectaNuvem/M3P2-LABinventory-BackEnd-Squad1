import json

from random import randint
from src.app.database.seeds import seeds


mimetype = "application/json"
url = "/employees/create"


headers = {"Content-Type": mimetype, "Accept": mimetype}


data = {
    "name": "João da Silva",
    "email": "teste54321" + str(randint(1, 1000)) + "@gmail.com",
    "phone": "1234567899",
    "position": "Desenvolvedor Backend",
    "gender": "Masculino",
    "zipcode": "85501-070",
    "birthDay": "2000-01-01",
    "city": "Pato Branco",
    "state": "PR",
    "neighborhood": "Centro",
    "street": "Rua Osvaldo Aranha",
    "houseNumber": 157,
    "complement": "123",
    "reference": "teste",
}


def test_create_employee_success(client, logged_in_client):
    data_copy = data.copy()
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "employees/create", data=json.dumps(data_copy), headers=headers
    )

    print(response.json, "response")

    assert response.status_code == 201


def test_create_employee_missing_fields(client, logged_in_client):
    data_copy = data.copy()
    del data_copy["name"]
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "employees/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 400
    assert response.json["error"] == "Está faltando o item name"


def test_create_employee_invalid_cep_format(client, logged_in_client):
    data_copy = data.copy()
    data_copy["zipcode"] = "1234567899999"
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "/employees/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 400
    assert "O campo zipcode não está no formato correto" in response.json["error"]


def test_create_employee_invalid_name(client, logged_in_client):
    data_copy = data.copy()
    data_copy["name"] = "ab"
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "/employees/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 400
    assert response.json["error"] == "O campo name não está no formato correto"


def test_create_employee_invalid_email(client, logged_in_client):
    data_copy = data.copy()
    data_copy["email"] = "123@abc"
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "/employees/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 400
    assert response.json["error"] == "O campo email não está no formato correto"


def test_create_employee_invalid_phone(client, logged_in_client):
    data_copy = data.copy()
    data_copy["phone"] = "abc123456789"
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "/employees/create", data=json.dumps(data_copy), headers=headers
    )
    
    assert response.status_code == 400
    assert response.json["error"] == "O campo phone não está no formato correto"


def test_find_employee_by_name(client, logged_in_client):
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.get(
        "/employees/?searchField=name&searchValue=Ana", headers=headers
    )

    assert response.status_code == 200


def test_find_employee_by_id_success(client, logged_in_client):
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.get("/employees/6383746b0b9acf16803e273e", headers=headers)

    assert response.status_code == 200


def test_find_employee_by_id_not_found(client, logged_in_client):
    data_copy = data.copy()
    data_copy["phone"] = "abc123456789"
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.get(
        "/employees/?searchField=name&searchValue=Ana",
        data=json.dumps(data_copy),
        headers=headers,
    )

    assert response.status_code == 200


def test_update_employee_success(client):
    employees = seeds["employees"]
    data_copy = employees[0]
    data_copy["phone"] = "119999-9989"
    response = client.patch(
        "/employees/update", data=json.dumps(data), headers= headers
    )
    assert response.status_code == 400

