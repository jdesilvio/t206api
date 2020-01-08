"""Application tests."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import unittest

from t206api.app import create_app, db

from .factories import Session, TEST_DB_URI
from .factories.card_factory import CardFactory


class TestApp(unittest.TestCase):
    """Test application."""

    @classmethod
    def setUpClass(cls):
        """Set up class."""
        cls._app = create_app(TEST_DB_URI)
        cls._app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Tear down class."""
        os.remove('test.db')

    def setUp(self):
        """Set up tests."""
        self.app = self._app.test_client()
        self.app.testing = True
        with self._app.app_context():
            db.drop_all()
            db.create_all()
        self.session = Session()
        CardFactory.reset_sequence()

    def test_index(self):
        """Test index route."""
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'T206 Data API')

    def test_get_cards(self):
        """Test getting all cards."""
        CardFactory()
        CardFactory()
        self.session.commit()
        resp = self.app.get('cards')
        data = resp.json

        assert resp.status_code == 200
        assert len(data) == 2

    def test_get_card(self):
        """Test getting a specific card."""
        CardFactory()
        self.session.commit()
        resp = self.app.get('cards/1')

        assert resp.status_code == 200

    def test_create_card(self):
        """Test creating a new card."""
        data = {
            'first_name': 'Ty',
            'last_name': 'Cobb',
            'team_name': 'Detroit',
            'hof': True,
            'portrait': True,
            'horizontal': False
        }
        resp = self.app.post('cards', json=data)

        assert resp.status_code == 200

    def test_create_card_missing_name(self):
        """Test creating a new card without a name."""
        data = {
            'first_name': 'Ty',
        }
        resp = self.app.post('cards', json=data)

        assert resp.status_code == 500

    def test_update_card(self):
        """Test updating an existing card."""
        data = {
            'first_name': 'Ty',
            'last_name': 'Cobb',
        }
        CardFactory()
        self.session.commit()
        resp = self.app.put('cards/1', json=data)

        assert resp.status_code == 200

    def test_delete_card(self):
        """Test deleting a card."""
        CardFactory()
        self.session.commit()

        resp = self.app.get('cards/1')
        assert resp.status_code == 200
        resp = self.app.delete('cards/1')
        assert resp.status_code == 200
        resp = self.app.get('cards/1')
        assert resp.status_code == 404
