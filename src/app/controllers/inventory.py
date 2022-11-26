from bson import json_util
from flask import Blueprint, json, request
from flask.wrappers import Response

from src.app.services.inventory import Inventory_Service
from src.app.validators import adjust_errors_from_mongoschema

inventory = Blueprint("inventory", __name__, url_prefix="/inventory")
inventorys_service = Inventory_Service()


@inventory.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    response = inventorys_service.create_inventory(data, "items")

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(json_util.dumps(response), status=201, mimetype="application/json")


@inventory.route("/", methods=["GET"])
def get_all():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 8, type=int)
    search_field = request.args.get("searchField", None, type=str)
    search_value = request.args.get("searchValue", None, type=str)
    operator = request.args.get("operator", None, type=str)
    payload = {}
    if page and limit:
        payload = {
            "filter": {search_field: search_value} if search_field else {},
            "operator": operator,
            "skip": (page - 1) * (limit),
            "limit": limit,
        }
    response = inventorys_service.get_inventory(payload)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/<id>", methods=["GET"])
def get_by_id(id):
    response = inventorys_service.get_inventory_by_id(id)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/list", methods=["GET"])
def list():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 8, type=int)
    search_field = request.args.get("searchField", None, type=str)
    search_value = request.args.get("searchValue", None, type=str)
    operator = request.args.get("operator", None, type=str)
    payload = {}
    if page and limit:
        payload = {
            "filter": {search_field: search_value} if search_field else {},
            "operator": operator,
            "skip": (page - 1) * (limit),
            "limit": limit,
        }
    response = inventorys_service.get_inventory_list(payload)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/update", methods=["PATCH"])
def update():
    data = request.get_json()
    response = inventorys_service.update_inventory(data, "items")

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/delete", methods=["DELETE"])
def delete():
    response = inventorys_service.delete_inventory(request.args)

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@inventory.route("/analytics", methods=["GET"])
def get_analytics():
    response = inventorys_service.get_analytics()

    if response is not None and "error" in response:
        status_return = response["status"] if "status" in response else 400
        return adjust_errors_from_mongoschema(response), status_return

    return Response(
        response=json.dumps(response), status=200, mimetype="application/json"
    )
