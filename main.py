from app import *
from email_validator import validate_email, EmailNotValidError


@app.route("/")
def create_table():
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
    try:
        if 'name' and 'email' in income_data:
            name = income_data['name']
            email = income_data['email']
            if not name.strip():
                return jsonify({"Error": {"name": "name field is Not be empty"}})
            if validate_email(email):
                user = EmployeeModel(name=name, email=email)
                db.session.add(user)
                db.session.commit()
                return jsonify("Name and Email added successfully")
        else:
            return jsonify("Both 'name' and 'email' field is required")

    except EmailNotValidError:
        return jsonify("Enter valid email address like - {}".format('example@gmail.com'))


@app.route('/update/<int:id>', methods=["PUT"])
def update(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'PUT':
        if employee:
            income_data = request.get_json()
            if 'name' and 'email' in income_data:
                name = income_data['name']
                email = income_data['email']
                try:
                    if not name.strip():
                        return jsonify({"Error": {"name": "name field is Not be empty"}})
                    validate_email(email)
                    employee.name = name
                    employee.email = email
                    db.session.commit()
                    return jsonify("User updated successfully")
                except EmailNotValidError:
                    return jsonify("Enter valid email address like - {}".format('example@gmail.com'))

            else:
                return jsonify("Both 'name' and 'email' field is required to update the user.")

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