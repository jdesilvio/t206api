"""Application tests."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from t206api.app import create_app


class TestApp(unittest.TestCase):
    """Test application."""

    @classmethod
    def setUpClass(cls):
        """Set up class."""
        cls._app = create_app()

    def setUp(self):
        """Set up tests."""
        self.app = self._app.test_client()
        self.app.testing = True

    def test_index(self):
        """Test index route."""
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'T206 Data API')
