def create_collection_roles(mongo_client):
  roles_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id","name", "description", "permissions"],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "Chave definida da collection"
            },
            "name": {
                "bsonType": "string",
                "description": "Abreviação da role",
            },
            "description": {
                "bsonType": "string",
                "description": "Nome da role"
            },
            "permissions": {
                "bsonType": "array",
                "description": "Permissões da role",
                "items": {
                    "bsonType": "string",
                    "description": "nome da permissão",
                }
            }
        },
    }
  }

  try:
    print("Criando a collection ROLES...")
    mongo_client.create_collection("roles")
    print("ROLES CRIADO COM SUCESSO.")
  except Exception as e:
    print(e)

  mongo_client.command("collMod", "roles", validator=roles_validator)