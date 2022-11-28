from bson import json_util
from flask import Blueprint, json, request
from flask.globals import session
from flask.wrappers import Response

from src.app.services.oauth2_services import callback_google, flow
from src.app.services.users_services import create_user, login_user, current_user

users = Blueprint("users", __name__, url_prefix="/users")


@users.route("/me", methods=["GET"])
def user_logged():
    token = request.headers.get("authorization", None)

    if not token:
        return Response(response=json.dumps({"erro": "Token inválido"}), status=401)

    response = current_user(token.replace("Bearer", "").strip())

    if "error" in response:
        return Response(
            response=json.dumps(response["error"]), status=response["status_code"]
        )

    return Response(response=json.dumps(response), status=200)


@users.route("/create", methods=["POST"])
def create():
    response = create_user(request.get_json())

    if "error" in response:
        return Response(
            response=json_util.dumps(response), status=400, mimetype="application/json"
        )

    return Response(
        response=json_util.dumps(response), status=201, mimetype="application/json"
    )


@users.route("/login", methods=["POST"])
def login():
    response = login_user(request.get_json())

    if "error" in response:
        return Response(
            response=json_util.dumps(response),
            status=response["status_code"],
            mimetype="application/json",
        )

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@users.route("/auth/google", methods=["POST"])
def auth_google():

    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return Response(
        response=json.dumps({"url": authorization_url}),
        status=200,
        mimetype="application/json",
    )


@users.route("/callback", methods=["GET"])
def callback():
    return callback_google()
