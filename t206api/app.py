"""Main application."""

# pylint: disable=unused-variable,import-error

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from flask import Flask, request, Response
from flask_migrate import Migrate

from .db import db
from .ma import ma
from .models import Card
from .schemas import card_schema, cards_schema


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = 'db.sqlite'
DB_URI = 'sqlite:///' + os.path.join(BASE_DIR, '..', DB_NAME)


def create_app():
    """Create the Flask application."""
    app = Flask(__name__.split('.')[1])
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

    # Setup database
    db.app = app
    db.init_app(app)
    Migrate(app, db)

    # Setup Marshmallow
    ma.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        """API description."""
        return Response('T206 Data API', mimetype='text/plain')

    @app.route('/cards', methods=['GET'])
    def get_cards():
        """Get all cards."""
        all_cards = Card.query.all()
        return cards_schema.jsonify(all_cards)

    @app.route('/cards/<int:card_id>', methods=['GET'])
    def get_card(card_id):
        """Get a card by id."""
        Card.query.get(card_id)

    @app.route('/cards', methods=['POST'])
    def create_card():
        """Create a card."""
        data = request.json
        card = Card(**data)
        db.session.add(card)
        db.session.commit()
        return card_schema.jsonify(card)

    @app.route('/cards/<int:card_id>', methods=['PUT'])
    def update_card(card_id):
        """Update a card."""
        data = request.json
        card = Card.query.get(card_id)

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        variety = data.get('variety')
        if first_name:
            card.first_name = first_name
        if last_name:
            card.last_name = last_name
        if variety:
            card.variety = variety

        db.session.commit()
        return card_schema.jsonify(card)

    @app.route('/cards/<int:card_id>', methods=['DELETE'])
    def delete_card(card_id):
        """Delete a card."""
        card = Card.query.get(card_id)
        db.session.delete(card)
        db.session.commit()
        return card_schema.jsonify(card)

    return app
