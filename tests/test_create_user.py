
from faker import Faker
import json

mimetype = 'application/json'
url = "/user/create"

headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
}

fake = Faker()


def test_successfully_create_user(client):
		data = {
			"email": fake.email(),
			"password": "12345678"
		}

		response = client.post("users/create", data=json.dumps(data), headers=headers)

		assert response.status_code == 201
		assert response.json['message'] == "Usuário foi criado com sucesso."
  
  

def test_create_user_missing_fields(client):
		data = {
			"email": fake.email()
		}

		response = client.post("users/create", data=json.dumps(data), headers=headers)

		assert response.status_code == 400
		assert response.json['error'] == "Está faltando o item ['password']"
  
  
def test_create_user_with_existing_email(client):
		data = {
			"email": fake.email(),
			"password": "12345678"
		}

		client.post("users/create", data=json.dumps(data), headers=headers)
		response = client.post("users/create", data=json.dumps(data), headers=headers)

		assert response.status_code == 400
		assert response.json['error'] == "Usuário já existente!"
  
  
# def test_create_user_with_invalid_passwordl(client):
# 		data = {
# 			"email": fake.email(),
# 			"password": "12345"
# 		}

# 		response = client.post("users/create", data=json.dumps(data), headers=headers)

# 		assert response.status_code == 401
# 		assert response.json['error'] == "Suas credênciais estão incorretas!"
# 		assert response.json['status_code'] == 401