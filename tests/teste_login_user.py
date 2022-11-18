
from src.app import mongo_client

mimetype = 'application/json'
url = "/user/create"

headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

def test_create_user(client, logged_in_client):
    headers["Authorization"] = f"Bearer {logged_in_client}"

    assert isinstance(logged_in_client, str) == True