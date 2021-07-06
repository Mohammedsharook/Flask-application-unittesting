import unittest
import os
from api.route import app, db
from models.model import db


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('MYSQL_CONFIG')
        db.create_all()

    def test_case_1(self):
        res = app.test_client()
        resp = res.app.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_case_2(self):
        res = app.test_client()
        resp = res.app.get("/detail/1")
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()