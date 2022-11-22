from src.app.services import employees as employees_service
from flask import Blueprint, request
from flask.wrappers import Response
from bson import json_util
from src.app.validators import adjust_errors_from_mongoschema


employees = Blueprint("employees", __name__, url_prefix="/employees")
employee_service = employees_service.Employees_Service()


@employees.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    response = employee_service.create_employee(data, "employees")
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(json_util.dumps(response), status=201, mimetype="application/json")


@employees.route("/", methods=["GET"])
def get_all():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 8, type=int)
    searchField = request.args.get("searchField", None, type=str)
    searchValue = request.args.get("searchValue", None, type=str)
    operator = request.args.get("operator", None, type=str)
    payload = {}
    if page and limit:
        payload = {
            "filter": {searchField: searchValue} if searchField else {},
            "operator": operator,
            "skip": (page - 1) * (limit),
            "limit": limit,
        }
    response = employee_service.get_employees(payload)
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return response, status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employees.route("/<id>", methods=["GET"])
def get_by_id(id):
    response = employee_service.get_employee_by_id(id)
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )

@employees.route("/update", methods=["PATCH"])
def update():
    data = request.get_json()
    response = employee_service.update_employee(data, "employees")

    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employees.route("/delete", methods=["DELETE"])
def delete():
    response = employee_service.delete_employee(request.args)
    
    if response is not None and 'error' in response:
        status_return = response['status'] if 'status' in response else 400
        return adjust_errors_from_mongoschema(response), status_return
    
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )
