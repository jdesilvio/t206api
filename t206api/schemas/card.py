"""Card schema."""

# pylint: disable=invalid-name

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ..ma import ma


class CardSchema(ma.Schema):
    """Card schema definition."""

    class Meta:  # pylint: disable=no-init,old-style-class
        """Included fields."""

        fields = ('first_name', 'last_name', '_links')

    _links = ma.Hyperlinks({
        'collection': ma.URLFor('get_cards')
    })


card_schema = CardSchema()
cards_schema = CardSchema(many=True)
