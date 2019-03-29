"""Script to drop all tables and re-create them."""

from t206api.app import create_app
from t206api.db import db


if __name__ == '__main__':
    app = create_app()
    db.drop_all()
    db.create_all()
