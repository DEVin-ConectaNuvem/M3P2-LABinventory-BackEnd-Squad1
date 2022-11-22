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
    
def test_create_employer_invalid_cpf_format(employee):
    data = {
        "_id": fake._id(), 
        "name": fake.name(), 
        "birthDay": fake.birthDay(), 
        "email": fake.email(), 
        "phone": fake.phone(), 
        "gender": fake.gender(), 
        "zipcode": 1235, 
        "city": fake.city(), 
        "state": fake.state(), 
        "street": fake.street(), 
        "houseNumber": fake.houseNumber(), 
        "neighborhood": fake.neighborhood(), 
        "position": fake.position(), 
        "complement": fake.complement(), 
        "reference": fake.reference()
    }
    
    response = employee.post("employers/create", data=json.dumps(data), headers=headers)

    assert response.status_code == 400
    assert response.json['error'] == "Formato de CEP inválido!"