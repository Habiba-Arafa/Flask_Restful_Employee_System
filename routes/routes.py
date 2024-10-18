from flask import Blueprint, jsonify, request
from middleware.auth import authenicate_token

routes = Blueprint("routes", __name__)

employees = [
    {"id": 202201684, "name": "Habiba", "position": "Data Scientist"},
    {"id": 202201546, "name": "AYa", "position": "Software Engineer"},
    {"id": 202201245, "name": "Fatma", "position": "Machine Learning Engineer"},
]



@routes.before_request
def before_request():
    authenicate_token()



@routes.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)



@routes.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)
    if employee:
        return jsonify(employee)
    return jsonify({"message": "Employee not found"}), 404



@routes.route("/employees", methods=["POST"])
def create_employee():
    new_employee = request.json
    employees.append(new_employee)
    return jsonify(new_employee), 201



@routes.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)
    if employee:
        employee.update(request.json)
        return jsonify(employee)
    return jsonify({"message": "Employee not found"}), 404




@routes.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    global employees
    employees = [e for e in employees if e['id'] != employee_id]
    return jsonify({"message": "Employee deleted"}), 200
