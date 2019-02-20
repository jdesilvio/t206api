import unittest

from t206api.app import create_app


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._app = create_app()

    def setUp(self):
        self.app = self._app.test_client()
        self.app.testing = True

    def test_index(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'T206 Data API')
