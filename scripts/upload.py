"""Script to upload data to database."""

import csv

from t206api.models import Factory, Card

from t206api.app import create_app
from t206api.db import db


if __name__ == '__main__':
    app = create_app()

    with open('./data/factory.csv') as f:
        reader = csv.DictReader(f)
        for item in reader:
            factory = Factory(**item)
            db.session.add(factory)
            db.session.commit()
            print(factory.id, factory)
