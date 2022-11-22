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