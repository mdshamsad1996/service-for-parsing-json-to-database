"""
Application Layer
"""
from flask import jsonify


class QuizController():
    """
    Application layer for QuizController class
    """
    def __init__(self, manager):
        self.manager = manager

    def view_records(self) -> int:
        """
        View number of record
        """
        no_of_record = self.manager.fetchall()

        return jsonify({'number_of_records ': no_of_record})

    def add_record(self, requested_data) -> jsonify:
        """
        Add record
        """
        self.manager.add_record(requested_data)

        return jsonify({'message': "Successfully inserted"})
