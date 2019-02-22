"""
Card schema
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ..ma import ma


class CardSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'variety', '_links')

    _links = ma.Hyperlinks({
        'collection': ma.URLFor('get_cards')
    })

card_schema = CardSchema()
cards_schema = CardSchema(many=True)
