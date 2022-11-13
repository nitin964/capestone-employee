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
2. Use postman to hit link https://capestone-employee.herokuapp.com/employees with token.

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

## GET /questions

1. Returns success values, all categories and question.
2. Questions are paginated and 10 questions are returned in single execution.
3. Sample: curl http://127.0.0.1:5000/questions

Response
{\
  "categories": {\
    "1": "Science",\
    "2": "Art",\
    "3": "Geography",\
    "4": "History",\
    "5": "Entertainment",\
    "6": "Sports"\
  },\
  "currentCategory": null,\
  "questions": [\
    {\
      "answer": "Apollo 13",\
      "category": "5",\
      "difficulty": 4,\
      "id": 2,\
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"\
    },\
    {\
      "answer": "Tom Cruise",\
      "category": "5",\
      "difficulty": 4,\
      "id": 4,\
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"\
    },\
    {\
      "answer": "Maya Angelou",\
      "category": "4",\
      "difficulty": 2,\
      "id": 5,\
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"\
    },\
    {\
      "answer": "Edward Scissorhands",\
      "category": "5",\
      "difficulty": 3,\
      "id": 6,\
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"\
    },\
    {\
      "answer": "which",\
      "category": "1",\
      "difficulty": 1,\
      "id": 8,\
      "question": "this"\
    },\
    {\
      "answer": "Muhammad Ali",\
      "category": "4",\
      "difficulty": 1,\
      "id": 9,\
      "question": "What boxer's original name is Cassius Clay?"\
    },\
    {\
      "answer": "Brazil",\
      "category": "6",\
      "difficulty": 3,\
      "id": 10,\
      "question": "Which is the only team to play in every soccer World Cup tournament?"\
    },\
    {\
      "answer": "Uruguay",\
      "category": "6",\
      "difficulty": 4,\
      "id": 11,\
      "question": "Which country won the first ever soccer World Cup in 1930?"\
    },\
    {\
      "answer": "George Washington Carver",\
      "category": "4",\
      "difficulty": 2,\
      "id": 12,\
      "question": "Who invented Peanut Butter?"\
    },\
    {\
      "answer": "Lake Victoria",\
      "category": "3",\
      "difficulty": 2,\
      "id": 13,\
      "question": "What is the largest lake in Africa?"\
    }\
  ],\
  "success": true,\
  "totalQuestions": 43\
}

## DELETE /questions/{question_id}
1. Deletes the question of the given ID if it exists and it returns the deleted book, success value, total books, and book list based on current page number to update the frontend.
2. Sample: curl -X DELETE http://127.0.0.1:5000/questions/1

Response
{\
  "success": true\
}

## POST /add_questions

1. If all required inputs are provided then it will insert new question and it returns success values and generated id.
2. Sample: curl -X POST -H "Content-Type: application/json" -d "{""question"":""Heres a new question string"", ""answer"":""Heres a new answer string"", ""difficulty"":1, ""category"":3}" http://127.0.0.1:5000/add_questions

Reponse
{\
  "id": 15,\
  "success": true\
}

## POST /add_questions
1. It returns the searched items on the basis of input string, success value and total questions searched.
2. Sample: curl -X POST -H "Content-Type: application/json" -d "{""searchTerm"":""what""}" http://127.0.0.1:5000/search_questions

Response
{\
  "currentCategory": null,\
  "questions": [\
    {\
      "answer": "Muhammad Ali",\
      "category": "4",\
      "difficulty": 1,\
      "id": 9,\
      "question": "What boxer's original name is Cassius Clay?"\
    },\
    {\
      "answer": "Tom Cruise",\
      "category": "5",\
      "difficulty": 4,\
      "id": 4,\
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"\
    },\
    {\
      "answer": "Edward Scissorhands",\
      "category": "5",\
      "difficulty": 3,\
      "id": 6,\
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"\
    },\
    {\
      "answer": "Lake Victoria",\
      "category": "3",\
      "difficulty": 2,\
      "id": 13,\
      "question": "What is the largest lake in Africa?"\
    },\
    {\
      "answer": "Mona Lisa",\
      "category": "2",\
      "difficulty": 3,\
      "id": 17,\
      "question": "La Giaconda is better known as what?"\
    },\
    {\
      "answer": "The Liver",\
      "category": "1",\
      "difficulty": 4,\
      "id": 20,\
      "question": "What is the heaviest organ in the human body?"\
    },\
    {\
      "answer": "Blood",\
      "category": "1",\
      "difficulty": 4,\
      "id": 22,\
      "question": "Hematology is a branch of medicine involving the study of what?"\
    }\
  ],\
  "success": true,\
  "totalQuestions": 7\
}

## GET /categories/{category_id}/questions

1. Returns questions related to the category id passed in the URL, success value and count of returned questions.
2. Sample: curl http://127.0.0.1:5000/categories/1/questions

Response
{\
  "current_category": 1,\
  "questions": [\
    {\
      "answer": "The Liver",\
      "category": "1",\
      "difficulty": 4,\
      "id": 20,\
      "question": "What is the heaviest organ in the human body?"\
    },\
    {\
      "answer": "Alexander Fleming",\
      "category": "1",\
      "difficulty": 3,\
      "id": 21,\
      "question": "Who discovered penicillin?"\
    },\
    {\
      "answer": "Blood",\
      "category": "1",\
      "difficulty": 4,\
      "id": 22,\
      "question": "Hematology is a branch of medicine involving the study of what?"\
    },\
    {\
      "answer": "which",\
      "category": "1",\
      "difficulty": 1,\
      "id": 8,\
      "question": "this"\
    },\
    {\
      "answer": "which",\
      "category": "1",\
      "difficulty": 1,\
      "id": 25,\
      "question": "this"\
    },\
    {\
      "answer": "lates",\
      "category": "1",\
      "difficulty": 1,\
      "id": 28,\
      "question": "latest"\
    },\
    {\
      "answer": "which",\
      "category": "1",\
      "difficulty": 1,\
      "id": 29,\
      "question": "latest"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 30,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 32,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 34,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 36,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 38,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 40,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 42,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 44,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 46,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 48,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 50,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 52,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 54,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 56,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 58,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 60,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 62,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 64,\
      "question": "insert question"\
    },\
    {\
      "answer": "insert answer",\
      "category": "1",\
      "difficulty": 1,\
      "id": 66,\
      "question": "insert question"\
    }\
  ],\
  "success": true,\
  "total_questions": 26\
}

## POST /quizzes

1. It returns the random questions which were not fetched earlier during the play along with success value.
2. Sample: curl -X POST -H "Content-Type: application/json" -d "{""previous_questions"": [1,4,20,15], ""quiz_category"": {""type"": ""click"", ""id"": []}}" http://127.0.0.1:5000/quizzes

Response
{\
  "question": {\
    "answer": "Alexander Fleming",\
    "category": "1",\
    "difficulty": 3,\
    "id": 21,\
    "question": "Who discovered penicillin?"\
  },\
  "success": true\
}
