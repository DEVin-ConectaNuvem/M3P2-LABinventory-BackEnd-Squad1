import random

import requests
from flask import current_app, request
from flask.globals import session
from google import auth
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from werkzeug.utils import redirect

from src.app import mongo_client
from src.app.services.users_services import create_user
from src.app.utils import generate_jwt


def callback_google():

    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    request_session = requests.session()
    token_google = auth.transport.requests.Request(session=request_session)

    user_google_dict = id_token.verify_oauth2_token(
        id_token=credentials.id_token,
        request=token_google,
        audience=current_app.config["GOOGLE_CLIENT_ID"],
    )

    user = mongo_client.users.find_one({"email": user_google_dict["email"]})

    password_gerado = gera_password()
    user_google_dict["password"] = password_gerado

    if user is None:
        create_user(user_google_dict)
        user = mongo_client.users.find_one({"email": user_google_dict["email"]})

    query_role = mongo_client.roles.find_one(user["role"])

    user_google_dict["user_id"] = str(user["_id"])
    user_google_dict["roles_description"] = query_role["description"]
    user_google_dict["roles_permissions"] = query_role["permissions"]

    session["google_id"] = user_google_dict.get("sub")

    del user_google_dict["aud"]
    del user_google_dict["azp"]

    token = generate_jwt(user_google_dict)

    return redirect(f"{current_app.config['FRONTEND_URL']}?jwt={token}")


flow = Flow.from_client_secrets_file(
    client_secrets_file="src/app/database/client_secret_credentials.json",
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid",
    ],
    redirect_uri="https://labinventary-ow6376zhsq-uc.a.run.app/users/callback",
)


def gera_password():
    letras = "abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ123456789"
    caracter = "!@#$%&^*-_"

    password = ""

    for i in range(0, 1):
        password_caracter = random.choice(caracter)
        password += password_caracter
        for h in range(0, 14):
            password_letras = random.choice(letras)
            password += password_letras
    return password
