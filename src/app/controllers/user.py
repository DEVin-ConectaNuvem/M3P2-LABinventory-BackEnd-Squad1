import json
from flask import Blueprint, request
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util

users = Blueprint("users", __name__,  url_prefix="/users")

@users.route("/create", methods = ["GET"])
def create():
    response = "Ainda em desenvolvimento"
    return Response(
    response=json_util.dumps(response),
    status=201,
    mimetype='application/json'
  )