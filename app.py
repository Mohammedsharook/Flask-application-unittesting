from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeeModel(db.Model):
    __tablename__ = "newtable"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))


