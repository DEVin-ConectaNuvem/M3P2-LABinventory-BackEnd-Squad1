
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