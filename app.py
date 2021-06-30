from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:9944394985@localhost/new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class EmployeeModel(db.Model):
    __tablename__ = "ayden"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))

