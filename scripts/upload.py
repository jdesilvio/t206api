"""Script to upload data to database."""

import csv

from t206api.models import Factory, Series, Team

from t206api.app import create_app
from t206api.db import db


def upload_data(filepath, model):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for item in reader:
            inst = model(**item)
            db.session.add(inst)
            db.session.commit()
            print(inst.id, inst)


if __name__ == '__main__':
    app = create_app()

    upload_data('./data/factory.csv', Factory)
    upload_data('./data/series.csv', Series)
    upload_data('./data/team.csv', Team)
