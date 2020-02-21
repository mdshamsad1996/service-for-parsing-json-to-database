"""
Routes module
"""
from flask import request, json
from src import app
from src.dependency_injector import DIQuiz
from src.controllers.quiz_controller import QuizController


di = DIQuiz()       # dependency object

quizcontroller = QuizController(di.get_quiz_manager())     # quizcontroller Object


@app.route('/api/add', methods=['POST'])
def add_quiz() -> str:
    """
    Adding quiz
    """
    data = request.data

    return quizcontroller.add_record(json.loads(data))


@app.route('/getrecords')
def get_records() -> int:
    """
    Get number of records
    """
    return quizcontroller.view_records()
