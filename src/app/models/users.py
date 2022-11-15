def create_collection_users(mongo_client):
  users_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "email", "password", "role"],
        "properties": {
            "_id": {
              "bsonType": "objectId",
              "description": "Chave definida da collection"
            },
            "email": {
              "bsonType": "string",
              "description": "Email do usuário",
            },
            "password": {
              "bsonType": "string",
              "description": "Senha do usuário"
            },
            "role": {
              "bsonType": "objectId",
              "description": "Vinculo da collection roles",
            }
        },
    }
  }

  try:
    print("Criando a collection USERS...")
    mongo_client.create_collection("users")
    print("USERS CRIADO COM SUCESSO.")
  except Exception as e:
    print(e)

  mongo_client.command("collMod", "users", validator=users_validator)