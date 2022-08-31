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

