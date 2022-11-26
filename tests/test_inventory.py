import json

from faker import Faker

mimetype = "application/json"
url = "/inventory/create"

headers = {"Content-Type": mimetype, "Accept": mimetype}

fake = Faker()


def test_create_inventory_sucess(inventory):
    data = {
        "_id": fake._id(),
        "codPatrimonio": fake.codPatrimonio(),
        "title": fake.title(),
        "description": fake.description(),
        "category": fake.category(),
        "value": fake.value(),
        "brand": fake.brand(),
        "model": fake.model(),
        "collaborator": fake.collaborator(),
        "createdAt": fake.createdAt(),
        "updatedAt": fake.updatedAt(),
    }

    response = inventory.post(
        "inventory/create", data=json.dumps(data), headers=headers
    )

    assert response.status_code == 201


def test_create_inventory_missing_fields(inventory):
    data = {
        "_id": fake._id(),
        "codPatrimonio": fake.codPatrimonio(),
        "description": fake.description(),
        "category": fake.category(),
        "value": fake.value(),
        "brand": fake.brand(),
        "model": fake.model(),
        "collaborator": fake.collaborator(),
        "createdAt": fake.createdAt(),
        "updatedAt": fake.updatedAt(),
    }

    response = inventory.post(
        "inventory/create", data=json.dumps(data), headers=headers
    )

    assert response.staus_code == 400
    assert (
        response.json["error"] == "Está faltando algum campo requerido a ser preenchido"
    )
