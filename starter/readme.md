## Capestone - Employee

This API is to perform following actions on employee in coorporates.
1. Fetch list of employees
2. Delete employee
3. Modify employee details
4. Fetch employee details

## Getting Started

## Pre-requisites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.


## Starter

In local after creating virtual environment. Install requirement.txt. All requireed packages are included in the requirements file.

To run the application in local use following command:
python app.py

The application will be deployed on http://127.0.0.1:5000/ by default.

To enable debug mode modify app.py with following code.
if __name__ == '__main__':
    app.run(debug = True)

For production deployment use below code.
if __name__ == '__main__':
    app.run()
App is also hosted on Heroku https://capestone-employee.herokuapp.com/

## API Reference
## Getting Started
1. Base URL of app on Heroku https://capestone-employee.herokuapp.com/ which is not coded and hence it will return resource not found.
2. Authentication: This version of the application does require authentication. So API needs to be registered/created in AUTH0. For this API, Manager and HR roles were created and assigned to two different users. To fetch tokens use following URL which is registered in AUTH0.

https://dev-qhqw-viy.us.auth0.com/authorize?audience=employee&response_type=token&client_id=SmWDEIzhvdJxynPvRBXqhkrIJDKqcfiu&redirect_uri=https://127.0.0.1:8080/logout

## Error Handling

Errors are returned as JSON objects in the following format:\
{\
    "success": False, \
    "error": 400, \
    "message": "bad request"\
}\
The API will return three error types when requests fail:
1. 400: Bad Request
2. 401: Unauthorized
3. 403: Permission not found
4. 404: Resource not Found
5. 405: Method not allowed
6. 422: Not processable

## Endpoints

## GET /employees
1. Returns employee designation, id, name and success status.
2. Use postman to hit link https://capestone-employee.herokuapp.com/employees with bearer token. METHODS="GET"

Response:
{\
    "employees": [\
        {\
            "designation": "Director1",\
            "id": 1,\
            "name": "Nitin1"\
        }\
    ],\
    "success": true\
}

## GET /employee/{Employee_id}

1. Returns success value with addresss, designation, dob, id and name of given employee ID.
2. Use postman to hit link https://capestone-employee.herokuapp.com/employees/1 with bearer token. METHODS="GET"

Response:
{\
    "employees": {\
        "address": "Rani Bagh",\
        "designation": "Director1",\
        "dob": "Tue, 28 Jun 1988 00:00:00 GMT",\
        "id": 1,\
        "name": "Nitin1"\
    },\
    "success": true\
}

## DELETE /employee/{employee_id}
1. Deletes the record of the given employee ID if it exists and it returns employee ID and success value.
2. Use postman to hit link https://capestone-employee.herokuapp.com/employees/1 with bearer token. METHODS="DELETE"

Response
{
    "employee": 2,
    "success": true
}

## POST /employee

1. If all required inputs are provided then it will insert new question and it returns success values and generated id.
2. Sample: https://capestone-employee.herokuapp.com/employee METHODS="POST"

Request:
{\
    "name": "Nitin1",\
    "dob": "1988-06-28",\
    "designation": "Director1",\
    "address": "Rani Bagh"\
}

Reponse:
{\
    "employee": 2,\
    "success": true\
}

## PATCH /employee/{employee_id}

1. If required inputs are provided then it will modify the employee details of given ID. It returns address, designation, dob, id, name and success value.
2. Sample: https://capestone-employee.herokuapp.com/employee/2 METHODS="PATCH"

Request:
{\
    "name": "Nitin1",\
    "dob": "1988-06-27",\
    "designation": "Sub-Director",\
    "address": "Delhi"\
}

Response:
{\
    "employee": {\
        "address": "Delhi",\
        "designation": "Sub-Director",\
        "dob": "Mon, 27 Jun 1988 00:00:00 GMT",\
        "id": 2,\
        "name": "Nitin1"\
    },\
    "success": true\
}
