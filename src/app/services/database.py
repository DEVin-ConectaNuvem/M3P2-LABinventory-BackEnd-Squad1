import json
from bson import ObjectId, json_util
from src.app import mongo_client

import re


class Database(object):
    def __init__(self, collection, validator=None):
        self.collection = collection
        self.validator = validator

    def create(self, data, validator=None):
        try:
            response = mongo_client[self.collection].insert_one(data)
            result = {"id": str(response.inserted_id)}
            return result
        except Exception as e:
            return {"error": str(e)}

    def get_one(self, data, validator=None):
        try:
            data_with_like = [
                {key: {"$regex": re.compile(value, re.IGNORECASE)}}
                for key, value in data.items()
            ]
            for item in data_with_like:
                data.update(item)
            response = mongo_client[self.collection].find_one(data)
            return response
        except Exception as e:
            return {"error": str(e)}

    def get_all(self, validator=None):
        try:
            response = mongo_client[self.collection].find()
            return response
        except Exception as e:
            return {"error": str(e)}

    def get_by_id(self, id, validator=None):
        try:
            response = mongo_client[self.collection].find_one(
                {"_id": ObjectId(id["id"])}
            )
            return response
        except Exception as e:
            return {"error": str(e)}

    def update(self, data, validator=None):
        try:
            id = {"_id": ObjectId(data["id"])}
            data_set = {"$set": data["dataset"]}
            response = mongo_client[self.collection].update_one(id, data_set)
            result = {"id": str(response.upserted_id)}
            return result
        except Exception as e:
            return {"error": str(e)}

    def delete(self, data, validator=None):
        try:
            response = mongo_client[self.collection].delete_one(data)
            return response
        except Exception as e:
            return {"error": str(e)}

    def count(self, data, validator=None):
        try:
            response = mongo_client[self.collection].count_documents(data)
            return response
        except Exception as e:
            return {"error": str(e)}
