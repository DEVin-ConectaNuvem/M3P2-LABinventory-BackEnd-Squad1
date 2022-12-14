import re

from src.app.models.employees import employees_validator
from src.app.models.items import items_validator
from src.app.models.users import users_validator

validators_source = {
    "items": items_validator,
    "employees": employees_validator,
    "users": users_validator,
}

convertTypes = {
    "string": [str],
    "objectId": [str],
    "int": [int],
    "double": [int, float],
    "bool": [bool],
    "list": [list],
    "dict": [dict],
    "null": [type(None)],
}


def decorator_validate_exist_item(funcao):
    def valida_exist_item(*args, **kwargs):
        data = args[1]
        collection = args[2]
        if collection.find_one({"_id": data["_id"]}) is not None:
            return {"error": "Item já existe na collection"}

    return valida_exist_item


def decorator_validate_types(f):
    def types_and_keys(*args, **kwargs):
        def validateRegex(regex, value):
            result = re.compile(regex).match(value)
            if result is None:
                return False
            return True

        object = args[1]
        collection = args[2]
        validate = validators_source[collection]
        for key in object:
            if key == "_id" or key == "id":
                continue
            elif (key != "dataset") and (
                key not in validate["$jsonSchema"]["properties"]
            ):
                return {"error": f"Chave {key} não existe na collection", "status": 400}
            elif (
                key != "dataset"
                and type(validate["$jsonSchema"]["properties"][key]["bsonType"]) == list
            ):
                validate_list = False
                for bsonType in validate["$jsonSchema"]["properties"][key]["bsonType"]:
                    if type(object[key]) in convertTypes[bsonType]:
                        validate_list = True
                    if "pattern" in validate["$jsonSchema"]["properties"][key]:
                        if (
                            validateRegex(
                                validate["$jsonSchema"]["properties"][key]["pattern"],
                                object[key],
                            )
                            == False
                        ):
                            return {
                                "error": f"O campo {key} não está no formato correto",
                                "status": 400,
                            }
                if validate_list == False:
                    return {
                        "error": f"O tipo do item {key} não é válido",
                        "status": 400,
                    }
            elif key == "dataset":
                for key in object["dataset"]:
                    if key not in validate["$jsonSchema"]["properties"]:
                        return {
                            "error": f"Chave {key} não existe na collection",
                            "status": 400,
                        }
                    elif (
                        type(validate["$jsonSchema"]["properties"][key]["bsonType"])
                        == list
                    ):
                        validate_list = False
                        for bsonType in validate["$jsonSchema"]["properties"][key][
                            "bsonType"
                        ]:
                            if type(object["dataset"][key]) in convertTypes[bsonType]:
                                validate_list = True
                        if validate_list == False:
                            return {
                                "error": f"O tipo do item {key} não é válido",
                                "status": 400,
                            }
                    elif (
                        type(object["dataset"][key])
                        in convertTypes[
                            validate["$jsonSchema"]["properties"][key]["bsonType"]
                        ]
                    ) == False:
                        return {
                            "error": f"O tipo do item {key} não é o mesmo da collection",
                            "status": 400,
                        }
            elif (
                type(object[key])
                in convertTypes[validate["$jsonSchema"]["properties"][key]["bsonType"]]
            ) == False:
                return {
                    "error": f"O tipo do item {key} não é o mesmo da collection",
                    "status": 400,
                }
            elif "pattern" in validate["$jsonSchema"]["properties"][key]:
                if (
                    validateRegex(
                        validate["$jsonSchema"]["properties"][key]["pattern"],
                        object[key],
                    )
                    == False
                ):
                    return {
                        "error": f"O campo {key} não está no formato correto",
                        "status": 400,
                    }
        return f(*args, **kwargs)

    return types_and_keys


def decorator_validate_required_keys(f):
    def valida_required_keys(*args, **kwargs):
        object = args[1]
        collection = args[2]
        validate = validators_source[collection]
        for key in validate["$jsonSchema"]["required"]:
            if key == "_id" or key == "id" or "dataset" in object:
                continue
            elif key not in object:
                return {"error": f"Está faltando o item {key}", "status": 400}
        return f(*args, **kwargs)

    return valida_required_keys


def adjust_errors_from_mongoschema(error):
    if "Document failed validation, full error" in error["error"]:
        return {"error": "Erro em validação - Contate o suporte", "status": 400}

    return error
