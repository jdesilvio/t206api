import os

from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = 'db.sqlite'
DB_URI = 'sqlite:///' + os.path.join(BASE_DIR, DB_NAME)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    variety = db.Column(db.String(256))

    def __repr__(self):
        variety = ' ({})'.format(self.variety) if self.variety else ''
        return "<Card [{}] '{} {}{}'>".format(
            self.id, self.first_name, self.last_name, variety)

    def __str__(self):
        variety = ' ({})'.format(self.variety) if self.variety else ''
        return '{} {}{}'.format(
            self.first_name, self.last_name, variety)


class CardSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'variety', '_links')

    _links = ma.Hyperlinks({
        'collection': ma.URLFor('get_cards')
    })

card_schema = CardSchema()
cards_schema = CardSchema(many=True)


@app.route('/', methods=['GET'])
def index():
    return 'T206 Data API'


@app.route('/cards', methods=['GET'])
def get_cards():
    all_cards = Card.query.all()
    return cards_schema.jsonify(all_cards)


@app.route('/cards/<int:card_id>', methods=['GET'])
def get_card(card_id):
    Card.query.get(card_id)


@app.route('/cards', methods=['POST'])
def create_card():
    data = request.json
    card = Card(**data)
    db.session.add(card)
    db.session.commit()
    return card_schema.jsonify(card)


@app.route('/cards/<int:card_id>', methods=['PUT'])
def update_card(card_id):
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
    card = Card.query.get(card_id)
    db.session.delete(card)
    db.session.commit()
    return card_schema.jsonify(card)


if __name__ == '__main__':
    app.run(debug=True)
