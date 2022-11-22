from faker import Faker
import json

mimetype = 'application/json'
url = '/inventory/create'

headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
}

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
    
    
    response = inventory.post("inventory/create", data=json.dumps(data), headers=headers)

    assert response.status_code == 201
    
def test_create_employer_invalid_cpf_format(inventory):
    data = {
        "_id": fake._id(), 
        "codPatrimonio": fake.name(), 
        "title": fake.birthDay(), 
        "description": fake.email(), 
        "category": fake.phone(), 
        "value": fake.gender(), 
        "brand": 1235, 
        "model": fake.city(), 
        "collaborator": fake.state(), 
        "createdAt": fake.street(), 
        "updatedAt": fake.houseNumber(), 
    }
    
    response = inventory.post("inventory/create", data=json.dumps(data), headers=headers)

    assert response.status_code == 400
    assert response.json['error'] == "Formato de CEP inválido!"