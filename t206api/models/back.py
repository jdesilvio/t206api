"""Back model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from sqlalchemy.dialects.postgresql import ENUM

from .series import serieses
from ..db import db


brand_types = (
    'American Beauty', 'Broad Leaf', 'Carolina Brights', 'Cycle',
    'Drum', 'El Principe de Gales', 'Hindu Brown', 'Lenox',
    'Old Mill', 'Piedmont', 'Polar Bear', 'Sovereign',
    'Sweet Caporal', 'Tolstoi', 'Ty Cobb Back', 'Uzit'
)
brand_enum = (ENUM(*brand_types, name='brand_type'))

variation_types = (
    'Apple Green', 'Forest Green', 'Brown', 'Black', 'Red',
    'Frame', 'No Frame', 'Southern League'
)
variation_enum = (ENUM(*variation_types, name='variation_type'))


class Back(db.Model):
    """Back model.

    Unique card backs.
    """

    id = db.Column(db.Integer, primary_key=True)

    # The brand of tabacco advertised on the back
    brand = db.Column(db.String(64), nullable=False)

    # The variation of the advertisement
    variation = db.Column(db.String(64), nullable=True)

    # Whether the factory was an overprint
    overprint = db.Column(db.Boolean, nullable=False)

    # The series that the back belongs to
    series = db.relationship(
        'Series', secondary=serieses, lazy='subquery',
        backref=db.backref('backs', lazy=True))

    # The description of the series on the back
    series_description = db.Column(db.String(64), nullable=False)

    # The factory that the card was printed in
    factory_id = db.Column(
        db.Integer, db.ForeignKey('factory.id'), nullable=False)

    def __repr__(self):  # pragma: no cover
        parts = [
            self.brand,
            self.variation,
            self.series_description,
            str(self.factory)
        ]
        back = ', '.join([part for part in parts if part is not None])
        return "<Back [{}] '{}'>".format(self.id, back)

    def __str__(self):  # pragma: no cover
        parts = [
            self.brand,
            self.variation,
            self.series_description,
            str(self.factory)
        ]
        back = ', '.join([part for part in parts if part is not None])
        return back



