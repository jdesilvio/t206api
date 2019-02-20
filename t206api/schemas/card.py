"""
Card schema
"""

from ..ma import ma


class CardSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'variety', '_links')

    _links = ma.Hyperlinks({
        'collection': ma.URLFor('get_cards')
    })

card_schema = CardSchema()
cards_schema = CardSchema(many=True)
