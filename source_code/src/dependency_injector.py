"""
Dependency injection module
"""
# import mysql.connector
import psycopg2
from src.datamanager.db_helper import DBHelper
from src.datamanager.data_store import DBDatastore

from src.domain.managers.quiz_manager import QuizManager


class DIQuiz():
    """
    Dependency Injection class
    """
    def __init__(self):
        """
        Connection with mysql is done
        """

        self.db_connection = psycopg2.connect(host='localhost',\
                                         database='quiz',\
                                         user='postgres',\
                                         port="5432",\
                                         password='shamsad@123')

        self.db_helper = DBHelper(self.db_connection)
        self.db_datastore = DBDatastore(self.db_helper)

    def get_db_helper_instance(self):
        """
        get db_helper instance
        """
        return self.db_helper

    def get_db_datastore_instance(self):
        """
        get db_datasore instance
        """
        return self.db_datastore

    def get_quiz_manager(self):
        """
        Get quiz manager instance
        """
        return QuizManager('quiz', self.get_db_datastore_instance())
