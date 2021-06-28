from flask import Flask, jsonify, request
from app import *
from email_validator import validate_email, EmailNotValidError
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:9944394985@localhost/new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
@app.route("/")
def create_table():
    db.create_all()
    return "<h1>Home Page</h1>"


@app.route("/detail/<int:user_id>")  # Read
def details(user_id):
    try:
        user = EmployeeModel.query.get(user_id)
        return jsonify({"Name": user.name, "Email": user.email})
    except AttributeError:
        return jsonify('NO USER FOUND AT ID {}'.format(user_id))


@app.route('/login', methods=['POST'])     # create
def login():
    income_data = request.get_json()
    name = income_data['name']
    email = income_data['email']
    if name is None or len(name) < 1:
        return jsonify("Name field is required, Not be empty", {"name": "your_name"})
    try:
        if validate_email(email):
            user = EmployeeModel(name=name, email=email)
            db.session.add(user)
            db.session.commit()
            return jsonify("Name and Email added successfully")

    except EmailNotValidError:
        return jsonify("Enter valid email address like - {}".format('example@gmail.com'))


@app.route('/update/<int:id>', methods=["PUT"])
def update(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'PUT':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            income_data = request.get_json()
            name = income_data['name']
            email = income_data['email']
            if email is not None and validate_email(email):
                user = EmployeeModel(id=id, name=name,email=email)
                db.session.add(user)
                db.session.commit()
                return jsonify("USer updated successfully")
            else:
                return jsonify("Enter valid email id or email is required")
        return jsonify("User id not exists")


@app.route('/delete/<int:id>', methods=['delete'])    # delete
def delete(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'DELETE':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return jsonify("User deleted successfully")
        else:
            return jsonify("User ID not exists")


if __name__ == '__main__':
    app.run(debug=True)