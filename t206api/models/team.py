"""Team model.

Teams model and teams-to-card mapping table.
"""

# pylint: disable=invalid-name

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ENUM

from ..db import db


league_types = ('National', 'American', 'Southern', 'Minor')
league_enum = (ENUM(*league_types, name='league_type'))


class Team(db.Model):
    """A team that a player belongs to.

    The normalized team and assocaite league.
    City names are normalized to the full name
    of the city.
    """

    id = db.Column(db.Integer, primary_key=True)

    # The city of the team
    city = db.Column(db.String(64), nullable=False)

    # The league of the team
    league = db.Column(db.String(64), nullable=False)

    def __repr__(self):  # pragma: no cover
        return "<Team [{}] '{}, {}'>".format(
            self.id, self.city, self.league)

    def __str__(self):  # pragma: no cover
        return '{}, {}'.format(self.city, self.league)


teams = db.Table('teams',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
    db.Column('card_id', db.Integer, db.ForeignKey('card.id'), primary_key=True)
)
