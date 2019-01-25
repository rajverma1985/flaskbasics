from flask import Flask
from connection import app
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy(app)

class Laptop(db.Model):
    __tablename__= 'flasktable'
    name = db.Column(db.String(100), unique=False, nullable=False)
    ID = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=False, nullable=False)
    type = db.Column(db.String(100), unique=False, nullable=True)
    company = db.Column(db.String(100), unique=False, nullable=True)

#add the laptop entry to the database

def add_laptop(_name,_price, _ID, _company, _type):
    newlaptop=Laptop(name=_name, price=_price, ID=_ID, company=_company, type=_type)
    db.session.add(newlaptop)
    db.session.commit()


def getlaptopinfo():
    return Laptop.query.all()
