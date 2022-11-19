from faker import Faker
import json

mimetype = 'application/json'
url = "/user/create"

headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
}

fake = Faker()


def test_login_user_successfully(client):
    data = {
        "email": fake.email(),
        "password": "12345678"
    }

    response = client.post("users/create", data=json.dumps(data), headers=headers)

    assert response.status_code == 201
    assert response.json['message'] == "Usuário foi criado com sucesso."

    response = client.post("users/login", data=json.dumps(data), headers=headers)
    
    assert response.status_code == 200
    assert isinstance(response.json['token'], str)

  
