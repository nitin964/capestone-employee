import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from models import setup_db
from flask_cors import CORS
from models import setup_db, Employee
from auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    #This endpoint is to extract employees list
    @app.route("/employees")
    @requires_auth('get:employees')
    def retrieve_employees(jwt):
        selection = Employee.query.order_by(Employee.id).all()
        return jsonify(
            {
                'success': True,
                'employees': [employee.employees() for employee in selection]
            }
        )

    #This endpoint is to extract employee details
    @app.route("/employee/<int:employee_id>")
    @requires_auth('get:employee-details')
    def retrieve_employee_details(jwt,employee_id):
        selection = Employee.query.get(employee_id)
        if selection is None:
            abort(404)

        return jsonify(
            {
                'success': True,
                'employees': selection.employeedetails()
            }
        )

    #This endpoint is to add employee
    @app.route("/employee", methods=["POST"])
    @requires_auth('post:employee')
    def add_employee(jwt):
        body = request.get_json()
        new_name = body.get("name", None)
        new_dob = body.get("dob", None)
        new_designation = body.get("designation", None)
        new_address = body.get("address", None)

        if new_name in (None, ''):
            abort(422)
        if new_dob in (None, ''):
            abort(422)
        if new_designation in (None, ''):
            abort(422)
        if new_address in (None, ''):
            abort(422)

        try:
            employee = Employee(name=new_name, dob=new_dob, designation=new_designation, address=new_address)
            employee.insert()

            return jsonify({
                'success': True,
                'employee': employee.id
            })
        except:
            abort(422)

    #This endpoint is to update employee
    @app.route("/employee/<int:employee_id>", methods=["PATCH"])
    @requires_auth('patch:employee')
    def modify_employee(jwt, employee_id):
        employee = Employee.query.get(employee_id)
        
        if employee is None:
            abort(404)
        
        try:
            body = request.get_json()
            if 'name' in body:
                employee.name = body.get("name")
            if 'dob' in body:
                employee.dob = body.get("dob")
            if 'name' in body:
                employee.designation = body.get("designation")
            if 'name' in body:
                employee.address = body.get("address")        
            employee.update()
            
            return jsonify({
                'success': True,
                'employee': employee.employeedetails()
            })
        except:
            abort(422)

    #This endpoint is to delete employee
    @app.route("/employee/<int:employee_id>", methods=["DELETE"])
    @requires_auth('delete:employee')
    def delete_employee(jwt, employee_id):
        employee = Employee.query.get(employee_id)
        
        if employee is None:
            abort(404)
        
        try:
            employee.delete()

            return jsonify({
                'success': True,
                'employee': employee_id
            })
        except:
            abort(422)

    # Error Handling for 400
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    # Error Handling for 401
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    # Error Handling for 400
    @app.errorhandler(403)
    def permission_not_found(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "permission not found"
        }), 403

    # Error Handling for 404
    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    # Error Handling for 405
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    # Error Handling for 422
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
        
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)