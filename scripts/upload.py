"""Script to upload data to database."""

import csv

from t206api.models import Card, Factory, Series, Team, Variation
from t206api.models.team import teams

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


def upload_cards(filepath):
    bool_fields = ['hof', 'portrait', 'horizontal']
    null_fields = ['lipset_number', 'pose']

    with open(filepath) as f:
        reader = csv.DictReader(f)
        for item in reader:

            for bool_field in bool_fields:
                if item[bool_field] == 'TRUE':
                    item[bool_field] = True
                if item[bool_field] == 'FALSE':
                    item[bool_field] = False

            for null_field in null_fields:
                if item[null_field] == '':
                    item[null_field] = None

            card = Card(**item)
            db.session.add(card)
            db.session.commit()
            print(card.id, card)


def upload_card_teams(filepath):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for item in reader:
            card = Card.query.filter_by(
                first_name=item['first_name'],
                last_name=item['last_name'],
                pose=item['pose'] if item['pose'] else None
            ).one()

            team = Team.query.filter_by(
                city=item['city'],
                league=item['league']
            ).one()

            db.session.execute(
                teams.insert().values(
                    card_id=card.id, team_id=team.id))


def upload_variations(filepath):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for item in reader:
            card = Card.query.filter_by(
                first_name=item['first_name'],
                last_name=item['last_name'],
                pose=item['pose'] if item['pose'] else None
            ).one()

            variation = Variation(
                card_id=card.id,
                description=item['description'])

            db.session.add(variation)
            db.session.commit()
            print(variation.id, variation)


if __name__ == '__main__':
    app = create_app()

    upload_data('./data/factory.csv', Factory)
    upload_data('./data/series.csv', Series)
    upload_data('./data/team.csv', Team)
    upload_cards('./data/card.csv')
    upload_card_teams('./data/card_teams.csv')
    upload_variations('./data/variation.csv')
