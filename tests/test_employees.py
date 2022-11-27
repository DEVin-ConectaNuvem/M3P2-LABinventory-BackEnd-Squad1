import json

mimetype = "application/json"
url = "/employees/create"

headers = {"Content-Type": mimetype, "Accept": mimetype}


data = {
    "name": "João da Silva",
    "email": "teste1234567@gmail.com",
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

def test_create_employee_email_already_exists(client):
    data_copy = data.copy()
    data_copy["email"] = "joaosilvaTeste@gmail.com"
    
    response = client.post(
        "/employees/create", data=json.dumps(data_copy), headers= headers
    )
    
    assert response.status_code == 400
    assert response.json["error"] == "Email informado já possui cadastro"