"""Card factory."""

import factory

from t206api.models import Card  # noqa: I202

from . import Session
from .base_factory import BaseFactory


class CardFactory(BaseFactory):
    """Card factory."""

    class Meta:  # pylint: disable=no-init
        """Card factory meta options."""

        model = Card
        sqlalchemy_session = Session

    first_name = 'Honus'
    last_name = 'Wagner'
    team_name = 'Pittsburgh'
    hof = False
    portrait = False
    horizontal = False
