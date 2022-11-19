import json

mimetype = 'application/json'

headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

def test_get_employers_success(client):

    response = client.get("employers/", headers=headers)

    assert response.status_code == 200
    assert response.json != []

def test_get_employers_by_name_success(client):

    data = {
        "name": "Luana"
    }

    response = client.get("employers/find", data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert data["name"] in response.json["name"]

def test_get_employers_by_name_not_found(client):

    data = {
        "name": "ZZZZ"
    }

    response = client.get("employers/find", data=json.dumps(data), headers=headers)

    assert response.status_code == 200
