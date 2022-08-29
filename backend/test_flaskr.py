import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('postgres:abc@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": "Who create python programming language",
            "answer": "Guido Van Rossum",
            "difficulty": "1",
            "category": "1"
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginated_questions(self):
        """
        Test get_paginated_questions
        """
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["questions"])
        self.assertTrue(len(data["questions"]))

    def test_404_sent_requesting_beyond_valid_page(self):
        """
        Test that the beyond valid_page param is passed to get_paginated_questions
        """
        res = self.client().get("/books?page=1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


    def test_get_categories(self):
        """
        Test the get_categories method
        """
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["categories"])
        self.assertTrue(len(data["categories"]))


#     def test_delete_question(self):
#         """
#         Test deleting a question
#         """
#         res = self.client().delete("/questions/16")
#         data = json.loads(res.data)
#
#         question = Question.query.filter(Question.id == 16).first()
#
#         self.assertEqual(res.status_code, 200)
#         self.assertEqual(data["deleted"], 16)
#         self.assertTrue(data["total_questions"])
#         self.assertTrue(len(data["questions"]))
#         self.assertEqual(question, None)

    def test_422_if_question_does_not_exist(self):
        """
        If a question does not exist, an error should be thrown.
        """
        res = self.client().delete("/questions/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_add_new_question(self):
        """
        Test adding a new question
        """
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["question"])
        self.assertTrue(data["answer"])
        self.assertTrue(data["category"])
        self.assertTrue(data["difficulty"])

    def test_405_if_question_adding_not_allowed(self):
        """
        Test If a question is not allowed, an error should be thrown.
        """

        res = self.client().post("/questions/45", json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    def test_get_question_search_with_result(self):
        """
        Test searching for questions with search term with result
        """
        res = self.client().post("/questions", json={"searchTerm":"what"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])

    def test_get_question_search_without_result(self):
        """
        Test searching for questions with search term without result
        """
        res = self.client().post("/questions", json={"searchTerm":"opeyemi"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertFalse(data["questions"])
        self.assertFalse(data["total_questions"])

    def test_get_questions_by_category(self):
        """
        Test getting questions by category
        """
        res = self.client().get("/categories/2/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["questions"])
        self.assertTrue(data["current_category"])
        self.assertTrue(data["total_questions"])

    def test_422_if_category_does_not_exist(self):
        """
        Test getting questions by category and category does not exist
        """
        res = self.client().get("/categories/7777/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")









# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
