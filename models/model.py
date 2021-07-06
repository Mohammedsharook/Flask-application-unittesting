from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    job = db.relationship('JobRole', backref='user', uselist=False)


class JobRole(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


db.create_all()
db.session.commit()