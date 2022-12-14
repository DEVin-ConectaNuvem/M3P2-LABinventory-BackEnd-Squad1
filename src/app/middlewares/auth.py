from functools import wraps

from flask import current_app, jsonify, request
from jwt import decode

from src.app import mongo_client


def requires_access_level(permission):
    def jwt_required(function_current):
        @wraps(function_current)
        def wrapper(*args, **kwargs):
            token = None

            if "authorization" in request.headers:
                token = request.headers["authorization"]

            if not token:
                return (
                    jsonify({"error": "Você não tem permissão para acessar essa rota"}),
                    403,
                )

            if not "Bearer" in token:
                return (
                    jsonify({"error": "Você não tem permissão para acessar essa rota"}),
                    401,
                )

            try:
                token_pure = token.replace("Bearer ", "")
                decoded = decode(token_pure, current_app.config["SECRET_KEY"], "HS256")
            except Exception:
                return jsonify({"error": "O token é inválido"}), 403

            found_permission = 0

            query_role = mongo_client.roles.find_one(
                {"description": decoded["roles_description"]}
            )

            for permissions in query_role["permissions"]:
                if permissions in permission:
                    found_permission = found_permission + 1

            if found_permission < len(permission):
                return (
                    jsonify(
                        {"error": "Você não tem permissão para essa funcionalidade"}
                    ),
                    403,
                )

            return function_current(*args, **kwargs)

        return wrapper

    return jwt_required
