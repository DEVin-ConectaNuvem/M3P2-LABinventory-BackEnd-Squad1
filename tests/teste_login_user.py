
from src.app import mongo_client

mimetype = 'application/json'
url = "/user/create"

headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

def test_create_user(client, create_user_in_client):
    headers["Authorization"] = f"Bearer {create_user_in_client}"

    assert create_user_in_client == True