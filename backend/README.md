# Trivia App API

## Introduction

This API allows you manage a pool of questions and categories for a Trivia App.

## Getting Started

This API is currently not deployed to a remote server and has to be run locally to be used. <br/>

**BASE URL**: `http://localhost:5000`

## Error Handling

### Response Object

Errors are returned as JSON in the following format:

```
{
    "error": 404,
    "message": "The requested resource was not found."
}
```

### Response Keys

`error` - Status code of the error that occurred. <br>
`message` - Accompanying error message.

### Status Codes

`400 (Bad request)` - Your request was not properly formatted. <br>
`404 (Not found)` - The requested resource was not found. <br>
`422 (Unprocessable)` - The server understood your request but it could not be processed. <br>
`500 (Internal server error)` - Something went wrong on the server. <br>


## Endpoint Library

### Categories

### `GET /categories`

This fetches all the question categories as an object with each category's id as the key and type as value.

#### Query Parameters

This endpoint takes in no query parameter.

#### Request Body

This endpoint doesn't require a request body.

#### Sample Request

`curl http://localhost:5000/categories`

#### Sample Response

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

### Questions

### `GET /questions`

This returns a paginated list of all questions within the database along, all categories and the total number of questions. Each page contains a maximum of 10 questions.

#### Query Parameters

`page`: int <small> (optional) </small> - Page number starting from 1.

#### Request Body

This endpoint does not require a request body

#### Sample Request

`curl http://localhost:5000/questions?page=2`

#### Sample Response

`questions`: array - Fetched questions. <br>
`totalQuestions`: int - Total number of questions in the database. <br>
`categories`: all categories

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    }
  ],
  "total_questions": 23
}
```

### `POST /questions`

This adds a question to the collection of questions in the database. It takes in the question, its category id, its difficulty rating and answer.

#### Query Parameters

This endpoint takes in no query parameters

#### Request Body

`question`: string <small> (required) </small> - Question text content. <br>
`answer`: string <small> (required) </small> - Answer to the question. <br>
`category`: int <small> (required) </small> - Category id of the question's category. <br>
`difficulty`:string <small> (required) </small> - Question's difficulty from 1 to 5. <br>

#### Sample Request

`curl http://127.0.0.1:5000/questions -X POST  -H "Content-Type: application/json" -d '{"question": "Who create python programming language?", "answer": "Guido Van Rossum", "category": "1", "difficulty": "2"}'`

#### Sample Response

```
{
  "answer": "Guido Van Rossum",
  "category": "1",
  "difficulty": "2",
  "question": "Who create python programming language?"
}
```

### `POST /questions` (SEARCH)

This performs a case insensitive search of questions from the database based on a search term. It returns an array of the questions and the total amount of questions that match the search term.

#### Query Parameters

This endpoint takes in no query parameters

#### Request Body

`searchTerm`: string <small> (required) </small> - Term to search for. <br>

`{ "searchTerm": "invent"}`

#### Sample Request

`curl http://127.0.0.1:5000/questions -X POST  -H "Content-Type: application/json" -d '{"searchTerm": "invent"}'`
#### Sample Response

`questions`: array - All questions that match the search term. <br>
`totalQuestions`: int - Total number of questions that match the search term. <br>


```
{
  "questions": [
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    }
  ],
  "total_questions": 1
}
```

### `DELETE /questions/{question_id}`

This deletes the question with the specified id. It returns a paginated list of all questions within the database along, all categories and the total number of questions. Each page contains a maximum of 10 questions and a success status.

#### Query Parameters

This endpoint takes in no query parameters.

#### Request Body

This endpoint requires no request body.

#### Sample Request

`curl http://127.0.0.1:5000/questions/20 -X DELETE`

#### Sample Response

`Success`: true
`questions`: array - Fetched questions. <br>
`totalQuestions`: int - Total number of questions in the database. <br>
`categories`: all categories

```
{
  "current_category": null,
  "deleted": 20,
  "questions": [
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 24
}
```

### Quizzes

### `POST /quizzes`

This returns a random question from the database within a specified category or from a random category if none is specified. It accepts an array of previous questions to ensure that a question that has been chosen before is not chosen again. If there are no other questions to left, it returns null.

#### Query Parameters

This endpoint takes in no query parameters

#### Request Body

`previous_questions`: array <small> (required) </small> - Contains ids of previously chosen questions. <br>
`quiz_category`: int <small> (optional) </small> - Current category. <br>

```
{
    "previous_questions": ['2', '13', '14', '15'],
    "quiz_category": {"id": "1", "type":"Science"}}
}
```

#### Sample Request

`curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":['2', '13', '14', '15'], "quiz_category": {"id": "1", "type":"Science"}}'`

#### Sample Response
`question`: object | None - randomly chosen question.

```
{
  "question": {
    "answer": "Guido Van Rossum",
    "category": 1,
    "difficulty": 2,
    "id": 56,
    "question": "Which country create python programming language?"
  },
  "success": true
}
```


























### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## ToDo Tasks
These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.


2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.


3. Create an endpoint to handle GET requests for all available categories.


4. Create an endpoint to DELETE question using a question ID.


5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.


6. Create a POST endpoint to get questions based on category.


7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.


8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.


9. Create error handlers for all expected errors including 400, 404, 422 and 500.



## Review Comment to the Students
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code.

Endpoints
GET '/api/v1.0/categories'
GET ...
POST ...
DELETE ...

GET '/api/v1.0/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
