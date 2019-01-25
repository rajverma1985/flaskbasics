from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://raj:test@123@localhost/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
