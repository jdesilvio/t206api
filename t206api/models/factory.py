"""Factory model."""

# pylint: disable=invalid-name

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ENUM

from ..db import db


district_types = ('1st District', '2nd District', '4th District')
district_enum = ENUM(*district_types, name='district_type')

state_types = ('Virginia', 'North Carolina', 'New York', 'Ohio')
state_enum = ENUM(*state_types, name='state_type')


class Factory(db.Model):
    """A factory that distributed cards."""

    __table_args__ = (UniqueConstraint('number', 'district', 'state'),)

    id = db.Column(db.Integer, primary_key=True)

    # The factory number
    number = db.Column(db.Integer, nullable=False)

    # The factory district
    district = db.Column(db.String(64), nullable=False)

    # The state the factory is in
    state = db.Column(db.String(64), nullable=False)

    def __repr__(self):  # pragma: no cover
        return "<Factory [{}] 'No. {}, {}, {}'>".format(
            self.id, self.number, self.district, self.state)

    def __str__(self):  # pragma: no cover
        return "Factory {}, {}, {}".format(
            self.number, self.district, self.state)
