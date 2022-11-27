import json

from bson import json_util

from src.app import mongo_client
from src.app.validators import (
    decorator_validate_required_keys,
    decorator_validate_types,
)

from .database import Database


class Inventory_Service:
    def __init__(self):
        self.db = Database("items")
        self.collection = "items"

    @decorator_validate_types
    @decorator_validate_required_keys
    def create_inventory(self, *args):
        try:
            data = args[0]
            cod_patrimonio = data["codPatrimonio"]
            exists_cod = self.db.get_one({"codPatrimonio": cod_patrimonio})

            if exists_cod:
                return {
                    "error": "O código de patrimonio informado já existe",
                    "status": 400,
                }

            return self.db.create(data)
        except Exception as e:
            return {"error": str(e)}

    def get_inventory(self, req_args=None):
        try:
            if req_args:
                return self.db.get_data_with_paginate(req_args)
            else:
                res = self.db.get_all()
                return res
        except Exception as e:
            return {"error": str(e)}

    def get_inventory_by_id(self, inventory_id):
        try:
            return self.db.get_by_id(inventory_id)
        except Exception as e:
            return {"error": str(e)}

    def get_inventory_list(self, req_args=None):
        try:
            all_employees = list(
                mongo_client["employees"].find({}, {"name": 1, "_id": 1, "email": 1})
            )
            list_employees_formated = Database.format_return(all_employees)
            all_items = []

            if req_args:
                all_items = self.db.get_data_with_paginate(req_args)
            else:
                all_items = self.db.get_all()

            result = {
                "rows": all_items["rows"],
                "totalRows": all_items["totalRows"],
                "employees": list_employees_formated,
            }

            return result
        except Exception as e:
            return {"error": str(e)}

    @decorator_validate_types
    @decorator_validate_required_keys
    def update_inventory(self, *args):
        try:
            data = args[0]
            if "codPatrimonio" in data["dataset"]:
                cod_patrimonio_initial = self.db.get_by_id(data["id"])["codPatrimonio"]
                cod_patrimonio = data["dataset"]["codPatrimonio"]
                if cod_patrimonio_initial != cod_patrimonio:
                    exists_cod = self.db.get_one({"codPatrimonio": cod_patrimonio})
                    if exists_cod:
                        return {
                            "error": "O código de patrimonio informado já existe",
                            "status": 400,
                        }

            return self.db.update(data)
        except Exception as e:
            return {"error": str(e)}

    def delete_inventory(self, inventory_id):
        try:
            return self.db.delete(inventory_id)
        except Exception as e:
            return {"error": str(e)}

    def get_analytics(self):
        try:
            total_value_items = mongo_client[self.collection].aggregate(
                [{"$group": {"_id": None, "totalValue": {"$sum": "$value"}}}]
            )
            total_items = mongo_client[self.collection].count_documents({})
            total_borrowed = mongo_client[self.collection].aggregate(
                [{"$match": {"collaborator": {"$ne": None}}}, {"$count": "borrowed"}]
            )
            total_collabs = mongo_client["employees"].count_documents({})

            json_total_value_items = json_util.dumps(total_value_items)
            json_total_items = json_util.dumps(total_items)
            json_total_borrowed = json_util.dumps(total_borrowed)
            json_total_collabs = json_util.dumps(total_collabs)

            response = {
                "total_value": json.loads(json_total_value_items)[0]["totalValue"],
                "total_items": json.loads(json_total_items),
                "total_borrowed": json.loads(json_total_borrowed)[0]["borrowed"] if json_total_borrowed != "[]" else 0,
                "total_collabs": json.loads(json_total_collabs),
            }
            return response
        except Exception as e:
            return {"error": str(e)}
