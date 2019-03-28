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
        card1 = CardFactory()
        self.session.commit()
        card2 = CardFactory()
        self.session.commit()
        resp = self.app.get('cards')
        data = resp.json

        assert resp.status_code == 200
        assert len(data) == 2

        assert data[0]['first_name'] == card1.first_name
        assert data[0]['last_name'] == card1.last_name
        assert data[0]['variety'] == card1.variety

        assert data[1]['first_name'] == card2.first_name
        assert data[1]['last_name'] == card2.last_name
        assert data[1]['variety'] == card2.variety

    def test_get_card(self):
        """Test getting a specific card."""
        card = CardFactory()
        self.session.commit()
        resp = self.app.get('cards/1')
        data = resp.json

        assert resp.status_code == 200

        assert data['first_name'] == card.first_name
        assert data['last_name'] == card.last_name
        assert data['variety'] == card.variety

    def test_create_card(self):
        """Test creating a new card."""
        data = {
            'first_name': 'Ty',
            'last_name': 'Cobb',
            'variety': 'green portrait'
        }
        resp = self.app.post('cards', json=data)

        assert resp.status_code == 200

        assert data['first_name'] == resp.json['first_name']
        assert data['last_name'] == resp.json['last_name']
        assert data['variety'] == resp.json['variety']

    def test_create_card_missing_variety(self):  # pylint: disable=invalid-name
        """Test creating a new card without a variety."""
        data = {
            'first_name': 'Ty',
            'last_name': 'Cobb',
        }
        resp = self.app.post('cards', json=data)

        assert resp.status_code == 200

        assert data['first_name'] == resp.json['first_name']
        assert data['last_name'] == resp.json['last_name']
        assert resp.json['variety'] is None

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
            'variety': 'green portrait'
        }
        CardFactory()
        self.session.commit()
        resp = self.app.put('cards/1', json=data)

        assert resp.status_code == 200

        assert data['first_name'] == resp.json['first_name']
        assert data['last_name'] == resp.json['last_name']
        assert data['variety'] == resp.json['variety']

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
