from app import app, User, JobRole, db
from flask import jsonify, request


@app.before_first_request
@app.route("/")
def home():
    db.create_all()
    return "<h1>Home Page</h1>"


@app.route("/detail/<int:user_id>")  # Read
def details(user_id):
    user = User.query.filter_by(id=user_id).first()
    job = JobRole.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify({"name": user.Name, "job_role": job.job}  )


@app.route('/login', methods=['POST'])
def login():
    income_data = request.get_json()
    if 'name' and 'job_role' in income_data:
        name = income_data['name']
        job_role = income_data['job_role']
        if not name.strip() or not job_role.strip():
            return jsonify({"Error": "name or job_role field is Not be empty"})
        user = User(Name=name)
        job = JobRole(job=job_role, user=user)
        db.session.add(user)
        db.session.add(job)
        db.session.commit()
        return jsonify("Name and job_role added successfully")
    else:
        return jsonify("Both 'name' and 'job_role' field is required")


@app.route('/update/<int:id>', methods=["PUT"])
def update(id):
    user = User.query.filter_by(id=id).first()
    if request.method == 'PUT':
        if user:
            income_data = request.get_json()
            if 'name' and 'job_role' in income_data:
                name = income_data['name']
                job_role = income_data['job_role']
                job = JobRole(job=job_role,user=user)
                JobRole.job = job
                user.Name = name
                db.session.commit()
                return jsonify("User Name and job_role is updated successfully")

            return jsonify("Both Name and Job_role  field is required to update the user.")
        return jsonify("User id not exists")


@app.route('/delete/<int:id>', methods=['delete'])    # delete
def delete(id):
    if request.method == "DELETE":
        user = User.query.filter_by(id=id).first()
        if request.method == "DELETE":
            if user:
                db.session.delete(user)
                db.session.commit()
                return jsonify("User deleted successfully")
            return jsonify("User Id Not Exists")


if __name__ == '__main__':
    app.run(debug=True)