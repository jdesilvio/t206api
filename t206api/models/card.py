"""
Card model
"""

from ..db import db


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
