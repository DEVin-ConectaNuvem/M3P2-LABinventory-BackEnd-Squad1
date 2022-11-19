from faker import Faker
import json

mimetype = 'application/json'
url = '/employers/create'

headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
}

fake = Faker()

def test_create_employers_missing_fields(employee):
    data = {
        "_id": fake._id(),
        "name": fake.name()
    }
    
    response = employee.post("employers/create", data=json.dumps(data), headers=headers)
    
    assert response.staus_code == 400
    assert response.json['error'] == "Está faltando algum item requerido"
    

