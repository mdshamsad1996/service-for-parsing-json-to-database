"""
Making src package
"""
from flask import Flask

app = Flask(__name__)

from src import routes
