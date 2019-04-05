"""Variation model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .team import teams
from ..db import db


class Variation(db.Model):
    """A card variation.

    Commonly recognized card variation. These are not
    unique designs. They are mostly printing errors
    that resulted in noticeable variations.
    """

    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)

    # The variation description
    description = db.Column(db.String(64), nullable=False)

    def __repr__(self):  # pragma: no cover
        return "<Variation [{}] '{} - {}'>".format(
            self.id, self.card, self.description)

    def __str__(self):  # pragma: no cover
        return '{} - {}'.format(
            self.card, self.description)
