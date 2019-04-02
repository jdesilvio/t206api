"""Card model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .team import teams
from ..db import db


class Card(db.Model):
    """A unique card front.

    There are 524 commonly recognized card designs.
    There are also a number of different varations
    caused by printing errors, name misspellings and
    breakdowns in the printing process.

    The nameplate is the bottom portion of a card that
    gives the player's name, team city and league.

    In some cases there are multiple teams on a single
    nameplate, these are also represented as having a single
    team name, but multiple team IDs.

    A design is defined as a unique combination of:
        * player
        * pose
        * team
    """

    id = db.Column(db.Integer, primary_key=True)

    # The number used in Lew Lipset's
    # "Encyclopedia of Baseball Cards, Volume 3"
    lipset_number = db.Column(db.Integer, nullable=True)

    # First name of the player depicted on the card
    first_name = db.Column(db.String(64), nullable=False)

    # Last name of the player depicted on the card
    last_name = db.Column(db.String(64), nullable=False)

    # The pose the player is taking in the image
    # The one exception to this is "Sherry Magie (Magee)"
    # where the pose is the same as the "Sherry Magee"
    # card, but the name is misspelled
    pose = db.Column(db.String(64), nullable=True)

    # A commonly recognized variation of the card, but
    # not a unique design
    variation = db.Column(db.String(256), nullable=True)

    # Team name as it appears on a nameplate (non-normalized)
    team_name = db.Column(db.String(64), nullable=False)

    # Whether the card is a portrait
    portrait = db.Column(db.Boolean, nullable=False)

    # Whether the card is horizontal (landscape)
    horizontal = db.Column(db.Boolean, nullable=False)

    # The team(s) the player is on
    teams = db.relationship(
        'Team', secondary=teams, lazy='subquery',
        backref=db.backref('cards', lazy=True))

    def __repr__(self):  # pragma: no cover
        pose = ' ({})'.format(self.pose) if self.pose else ''
        return "<Card [{}] '{}, {}{}'>".format(
            self.id, self.last_name, self.first_name, pose)

    def __str__(self):  # pragma: no cover
        pose = ' ({})'.format(self.pose) if self.pose else ''
        return '{}, {}{}'.format(
            self.last_name, self.first_name, pose)
