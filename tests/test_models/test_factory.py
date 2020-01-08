"""Factory model tests."""

import os
import unittest

from t206api.app import create_app, db
from t206api.models import Factory

from ..factories import Session, TEST_DB_URI
from ..factories.factory_factory import FactoryFactory


class TestFactoryModel(unittest.TestCase):
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
        FactoryFactory.reset_sequence()

    def test_create_factory(self):
        """Test creating a factory successfully."""
        factory = FactoryFactory()
        self.session.commit()

        factory_from_db = Factory.query.get(factory.id)

        factory_dict = factory.__dict__
        factory_from_db_dict = factory_from_db.__dict__

        factory_dict.pop('_sa_instance_state')
        factory_from_db_dict.pop('_sa_instance_state')

        self.assertDictEqual(factory_dict, factory_from_db_dict)
