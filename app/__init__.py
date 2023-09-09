# This code is setting up a Flask application with SQLAlchemy and cryptography libraries.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
cipher_suite = Fernet(app.config['SECRET_KEY'])

from app import routes
