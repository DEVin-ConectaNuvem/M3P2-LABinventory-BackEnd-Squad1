from flask import Blueprint, request
from flask.wrappers import Response
from bson import json_util
from src.app.services.users_services import create_user, login_user

users = Blueprint("users", __name__,  url_prefix="/users")

@users.route("/create", methods = ["POST"])
def create():
    response = create_user(request.get_json())

    if "error" in response:
        return Response(
            response=json_util.dumps(response),
            status=400,
            mimetype='application/json'
        )

    return Response(
        response=json_util.dumps(response),
        status=201,
        mimetype='application/json'
    )


@users.route('/login', methods = ["POST"])
def login():
  response = login_user(request.get_json())

  if "error" in response:
    return Response(
      response=json_util.dumps(response),
      status=response['status_code'],
      mimetype='application/json'
    )

  return Response(
      response=json_util.dumps(response),
      status=200,
      mimetype='application/json'
  )