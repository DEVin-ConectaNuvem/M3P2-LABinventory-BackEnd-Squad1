from src.app.database.seeds import seeds

employees_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "_id",
            "name",
            "birthDay",
            "email",
            "phone",
            "gender",
            "zipcode",
            "city",
            "state",
            "street",
            "houseNumber",
            "neighborhood",
            "position",
            "complement",
            "reference",
        ],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "Chave definida da collection",
            },
            "name": {
                "bsonType": "string",
                "pattern": "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]{3,99}$",
                "description": "Nome do colaborador",
            },
            "birthDay": {"bsonType": "string", "description": "Idade do colaborador"},
            "position": {"bsonType": "string", "description": "Cargo do colaborador"},
            "email": {
                "bsonType": "string",
                "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,10}$",
                "description": "Email do colaborador",
            },
            "phone": {
                "bsonType": "string",
                "pattern": "^[0-9]{10,11}$",
                "description": "Telefone do colaborador",
            },
            "gender": {"bsonType": "string", "description": "Genero do colaborador"},
            "zipcode": {
                "bsonType": "string",
                "pattern": "^[0-9]{5}-[0-9]{3}$",
                "description": "CEP do colaborador",
            },
            "city": {"bsonType": "string", "description": "Cidade do colaborador"},
            "state": {
                "bsonType": "string",
                "description": "Estado da residência do colaborador",
            },
            "street": {"bsonType": "string", "description": "Rua do colaborador"},
            "houseNumber": {
                "bsonType": "int",
                "minimum": 0,
                "description": "Número da rua do colaborador",
            },
            "neighborhood": {
                "bsonType": "string",
                "description": "bairro do colaborador",
            },
            "imageUser": {
                "bsonType": ["string", "null"],
                "description": "Imagem de perfil do colaborador",
            },
            "complement": {
                "bsonType": "string",
                "description": "Complemento do endereço do colaborador",
            },
            "reference": {
                "bsonType": "string",
                "description": "Ponto de referencia do colaborador",
            },
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


def create_collection_employees(mongo_client):
    try:
        print("Criando a collection employeeS...")
        mongo_client.create_collection("employees")
        if mongo_client.employees.count_documents({}) == 0:
            print("Gerando dados iniciais...")
            mongo_client.employees.insert_many(seeds["employees"])

        print("employeeS CRIADO COM SUCESSO.")
    except Exception as e:
        print(e)

    mongo_client.command("collMod", "employees", validator=employees_validator)
