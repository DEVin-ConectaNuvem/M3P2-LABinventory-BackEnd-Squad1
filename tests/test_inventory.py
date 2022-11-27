import json
from random import randint
from faker import Faker

mimetype = "application/json"
url = "/inventory/create"

headers = {"Content-Type": mimetype, "Accept": mimetype}

fake = Faker()

data = {
    "codPatrimonio": "teste123" + str(randint(1, 1000)),
    "title": fake.name(),
    "description": "Novo design com 11ª Geração de Processadores Intel Core i5-11300H",
    "category": "Computador",
    "value": 3499.99,
    "brand": "Lenovo",
    "model": "82MGS00200",
}


def test_create_inventory_sucess(client, logged_in_client):
    data_copy = data.copy()
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "inventory/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 201


def test_create_inventory_missing_fields(client, logged_in_client):
    data_copy = data.copy()
    del data_copy["title"]
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.post(
        "inventory/create", data=json.dumps(data_copy), headers=headers
    )

    assert response.status_code == 400
    assert response.json["error"] == "Está faltando o item title"

def test_create_inventory_invalid_value(client):
    data_copy = data.copy()
    data_copy["codPatrimonio"] = "mais um teste" + str(randint(1, 1000))
    data_copy["value"] = -1
    
    response = client.post(
        "inventory/create", data=json.dumps(data_copy), headers= headers
    )
    
    assert response.status_code == 400
    assert response.json["error"] == "Erro em validação - Contate o suporte"