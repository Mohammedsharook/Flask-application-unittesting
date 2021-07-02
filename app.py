import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_CONFIG")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    job = db.relationship('JobRole', backref='user', uselist=False)


class JobRole(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

