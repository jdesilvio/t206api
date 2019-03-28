"""Model instance facotries."""

# pylint: disable=invalid-name

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DB_NAME = 'test.db'
TEST_DB_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../..', TEST_DB_NAME)


engine = create_engine(TEST_DB_URI)
Session = scoped_session(sessionmaker(bind=engine))
