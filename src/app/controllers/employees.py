from src.app.services import employees as employees_service
from flask import Blueprint, request
from flask.wrappers import Response
from bson import json_util

employees = Blueprint("employees", __name__, url_prefix="/employees")
employee_service = employees_service.Employees_Service()


@employees.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    response = employee_service.create_employee(data, "employees")
    return Response(json_util.dumps(response), mimetype="application/json")


@employees.route("/find", methods=["GET"])
def get_find():
    data = request.get_json()
    response = employee_service.get_employee(data)
    return Response(json_util.dumps(response), status=200, mimetype="application/json")


@employees.route("/", methods=["GET"])
def get_all():
    page = request.args.get("page") or False
    limit = request.args.get("limit") or False
    payload = {}
    if page and limit:
        payload = {
            "filter": {},
            "skip": (int(page) - 1) * int(limit),
            "limit": int(limit),
        }
    response = employee_service.get_employees(payload)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employees.route("/getid", methods=["GET"])
def get_by_id():
    data = request.get_json()
    response = employee_service.get_employee_by_id(data)
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employees.route("/update", methods=["PATCH"])
def update():
    data = request.get_json()
    response = employee_service.update_employee(data, "employees")

    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )


@employees.route("/delete", methods=["DELETE"])
def delete():
    data = request.get_json()
    response = employee_service.delete_employee(data, "employees")
    return Response(
        response=json_util.dumps(response), status=200, mimetype="application/json"
    )
