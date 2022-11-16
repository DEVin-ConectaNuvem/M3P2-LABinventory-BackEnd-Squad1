from src.app.models.items import items_validator
from src.app.models.employers import employers_validator
from src.app.models.users import users_validator

validators_source = {
        "items": items_validator,
        "employers": employers_validator,
        "users": users_validator,
}

convertTypes ={
    "string": str,
    "objectId": str,
    "int": int,
    "double": float,
    "bool": bool,
    "array": list,
    "dict": dict,
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
        object = args[1]
        collection = args[2]
        validate = validators_source[collection]
        for key in object:
            if key == "_id" or key == "id":
                continue
            elif key == "dataset":
                for key in object["dataset"]:
                    if (type(object["dataset"][key]) == convertTypes[validate["$jsonSchema"]["properties"][key]["bsonType"]]) == False:
                        return {"error": f"O tipo do item {key} não é o mesmo da collection"}
            elif (type(object[key]) == convertTypes[validate["$jsonSchema"]["properties"][key]["bsonType"]]) == False:
                return {"error": f"O tipo do item {key} não é o mesmo da collection"}  
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

