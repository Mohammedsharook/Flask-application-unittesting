import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


app = create_app()
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_CONFIG")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

