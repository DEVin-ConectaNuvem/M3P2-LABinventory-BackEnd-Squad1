from src.app.services import inventory as inventory_service
from flask import Blueprint, request, json
from flask.wrappers import Response
from bson import json_util

inventory = Blueprint("inventory", __name__, url_prefix="/inventory")
inventoryService = inventory_service.inventoryService()

@inventory.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    response = inventoryService.create_inventory(data)
    return Response(json_util.dumps(response), status=201, mimetype="application/json")


@inventory.route("/find", methods=["GET"])
def get_find():
    data = request.get_json()
    response = inventoryService.find_inventory(data)
    return Response(json_util.dumps(response), status=200, mimetype="application/json")


@inventory.route("/", methods=["GET"])
def get_all():
    response = inventoryService.get_inventory()
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/getid", methods=["GET"])
def get_by_id():
    data = request.get_json()
    response = inventoryService.get_inventory_by_id(data)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/update", methods=["PATCH"])
def update():
    data = request.get_json()
    response = inventoryService.update_inventory(data)
    print(response)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/delete", methods=["DELETE"])
def delete():
    response = inventoryService.delete_inventory(request.args)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )

@inventory.route("/analytics", methods=["GET"])
def get_analytics():
    response = inventoryService.get_analytics()
    return Response(
        response=json.dumps(response),
        status=200,
        mimetype="application/json"
    )
