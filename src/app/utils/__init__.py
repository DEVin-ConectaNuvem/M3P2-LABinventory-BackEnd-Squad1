from flask_pymongo import PyMongo

mongo = PyMongo()

from flask import current_app
from jwt import encode


def exist_key(request_json, list_keys):
    keys_not_have_in_request = []

    for key in list_keys:
        if key in request_json:
            continue
        else:
            keys_not_have_in_request.append(key)

    if len(keys_not_have_in_request) == 0:
        return request_json

    return {"error": f"Está faltando o item {keys_not_have_in_request}"}


def generate_jwt(payload):
    token = encode(payload, current_app.config["SECRET_KEY"], "HS256")
    return token


def convert_id(object):
    try:
        if "_id" in object:
            object["id"] = str(object["_id"])
            del object["_id"]
        if "createdAt" in object:
            object["createdAt"] = str(object["createdAt"])
        if "updatedAt" in object:
            object["updatedAt"] = str(object["updatedAt"])

        return object
    except Exception as e:
        pass
