"""Series model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ..db import db


class Series(db.Model):
    """Groups of subjects.

    Cards were printed in several series. There are
    different subjects and backs in each series.
    """

    id = db.Column(db.Integer, primary_key=True)

    # The name of the series
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):  # pragma: no cover
        return "<Series [{}] '{}'>".format(self.id, self.name)

    def __str__(self):  # pragma: no cover
        return '{}'.format(self.name)


serieses = db.Table('serieses',
    db.Column('series_id', db.Integer, db.ForeignKey('series.id'), primary_key=True),
    db.Column('back_id', db.Integer, db.ForeignKey('back.id'), primary_key=True)
)
