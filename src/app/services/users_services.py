from datetime import datetime, timedelta

import bcrypt
from bson.objectid import ObjectId

from src.app import mongo_client
from src.app.utils import exist_key, generate_jwt, decode_jwt


class User:
    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

    @classmethod
    def seed(cls, email, password, role):
        user = User(email=email, password=password, role=role)
        user.password = user.encrypt_password(password.encode("utf-8"))
        user.save()

    @staticmethod
    def encrypt_password(password):
        return bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

    def save(self):
        roles_query = mongo_client.roles.find_one({"name": self.role})

        mongo_client.users.insert_one(
            {"email": self.email, "password": self.password, "role": roles_query["_id"]}
        )


def check_password(self, password):
    return bcrypt.checkpw(password.encode("utf-8"), self["password"].encode("utf-8"))


def login_user(request_data):
    try:
        list_keys = ["email", "password"]
        data = exist_key(request_data, list_keys)

        user_query = mongo_client.users.find_one({"email": data["email"]})

        if user_query is None:
            return {"error": "Suas credênciais estão incorretas!", "status_code": 401}

        role_query = mongo_client.roles.find_one({"_id": ObjectId(user_query["role"])})

        if not check_password(user_query, data["password"]):
            return {"error": "Suas credênciais estão incorretas!", "status_code": 401}

        payload = {
            "email": user_query["email"],
            "exp": datetime.utcnow() + timedelta(days=1),
            "roles_description": role_query["description"],
            "roles_permissions": role_query["permissions"],
        }

        token = generate_jwt(payload)

        return {"token": token}
    except Exception:
        return {"error": "Algo deu errado!", "status_code": 500}


def current_user(token):
    data = decode_jwt(token)
    
    user_query = mongo_client.users.find_one({"email": data["email"]})
    
    if user_query is None:
            return {"error": "Usuário não encontrado", "status_code": 404}
        
    role_query = mongo_client.roles.find_one({"_id": ObjectId(user_query["role"])})
    
    user_data = {
            "email": user_query["email"],
            "roles_description": role_query["description"],
            "roles_permissions": role_query["permissions"],
            "exp": data['exp']
        }
          
    
    return user_data


def create_user(request_data):
    try:
        list_keys = ["email", "password"]
        roles = ["ADMIN", "BACK_END", "FRONT_END", "FULLSTACK", "USER"]

        data = exist_key(request_data, list_keys)

        if "error" in data:
            return data

        if len(data["password"]) < 8:
            return {"error": "A senha deve ter no mínimo 8 caracteres"}

        exist_user = mongo_client.users.find_one({"email": data["email"]})

        if exist_user:
            return {"error": "Usuário já existente!"}

        role = "USER"

        if "role" in data:
            if data["role"] in roles:
                role = data["role"]

        User.seed(data["email"], data["password"], role)

        return {"message": "Usuário foi criado com sucesso."}
    except Exception:
        return {"error": "Algo deu errado!"}
