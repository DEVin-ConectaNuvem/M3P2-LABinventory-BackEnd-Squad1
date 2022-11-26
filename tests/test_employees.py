import json

mimetype = "application/json"
url = "/employees/create"

headers = {"Content-Type": mimetype, "Accept": mimetype}


data = {
    "name": "João da Silva",
    "email": "joaosilvaTeste@gmail.com",
    "phone": "(11) 9999-9999",
    "position": "Desenvolvedor Backend",
    "gender": "Masculino",
    "zipcode": "855010070",
    "birthDay": "2000-01-01",
    "city": "Pato Branco",
    "state": "PR",
    "neighborhood": "Centro",
    "street": "Rua Osvaldo Aranha",
    "houseNumber": 157,
    "complement": "123",
    "reference": "teste",
}


def test_create_employee_missing_fields(client):
    data_copy = data.copy()
    del data_copy["name"]
    response = client.post(
        "employees/create", data=json.dumps(data_copy), headers=headers
    )
    print(response, "response")
    assert response.status_code == 400
    assert response.json["error"] == "Está faltando o item name"


def test_create_employee_invalid_cep_format(client):
    data_copy = data.copy()
    data_copy["zipcode"] = "12345678999"

    response = client.post(
        "/employees/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 400
    assert response.json["error"] == "Erro em validação - Contate o suporte"

def test_create_employee_invalid_name(client):
    data_copy = data.copy()
    data_copy["name"] = "ab"

    response = client.post(
        "/employees/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 400
    assert response.json["error"] == "Erro em validação - Contate o suporte"
