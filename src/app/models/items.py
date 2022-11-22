items_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "_id",
            "codPatrimonio",
            "title",
            "description",
            "category",
            "value",
            "brand",
            "model",
        ],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "Chave definida da collection",
            },
            "codPatrimonio": {
                "bsonType": "string",
                "description": "Codigo de patrimonio do item",
            },
            "title": {"bsonType": "string", "description": "Titulo do item"},
            "category": {"bsonType": "string", "description": "Categoria do item"},
            "description": {"bsonType": "string", "description": "Descrição do item"},
            "value": {
                "bsonType": ["double", "int"],
                "minimum": 0,
                "description": "Valor do item",
            },
            "brand": {"bsonType": "string", "description": "Marca do item"},
            "model": {"bsonType": "string", "description": "Modelo do item"},
            "collaborator": {
                "bsonType": ["string", "null"],
                "description": "Colaborador que está com o item",
            },
            "url": {"bsonType": ["string", "null"], "description": "URL da imagem"},
            "createdAt": {
                "bsonType": "date",
                "description": "Data da criação do item",
            },
            "updatedAt": {
                "bsonType": "date",
                "description": "Data da última atualização",
            },
        },
    }
}


def create_collection_items(mongo_client):
    try:
        print("Criando a collection ITEMS...")
        mongo_client.create_collection("items")
        print("ITEMS CRIADO COM SUCESSO.")
    except Exception as e:
        print(e)

    mongo_client.command("collMod", "items", validator=items_validator)
