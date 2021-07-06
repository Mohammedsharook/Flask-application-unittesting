import json
import os
from api.route import app, db
import unittest


class FlaskTest(unittest.TestCase):

    def test_home(self):
        var = app.test_client()
        response = var.get("/")
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)

    def test_detail(self):
        var = app.test_client()
        resp = var.get('/detail/10')
        self.assertEqual(resp.status_code, 200)

    def test_login(self):
        var = app.test_client()
        resp = var.post('/login', data=json.dumps(dict(name='Mohammed Sharook', job_role="Engineer")),content_type='application/json')
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()