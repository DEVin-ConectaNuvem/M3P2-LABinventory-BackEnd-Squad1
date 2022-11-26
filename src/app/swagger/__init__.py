from flasgger import Swagger
from flask import Flask


def create_swagger(app: Flask):
    app.config["SWAGGER"] = {
        "openapi": "3.0.0",
        "title": "LABInventory API",
        "description": "API para trazer dados de usuarios, colaboradores e itens de um inventario.",
    }

    Swagger(app)
