import unittest

from webtest import TestApp

from restcraft_app.wsgi import application


class TestMyView(unittest.TestCase):
    def setUp(self):
        self.client = TestApp(application)

    def test_home(self):
        resp = self.client.get("/")
        self.assertEqual(resp.json, {"hello": "restcraft"})
