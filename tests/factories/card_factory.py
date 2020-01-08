"""Card factory."""

import factory

from t206api.models import Card  # noqa: I202

from . import Session


class CardFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Card factory."""

    class Meta:  # pylint: disable=no-init
        """Card factory meta options."""

        model = Card
        sqlalchemy_session = Session

    id = factory.Sequence(lambda n: n)
    first_name = 'Honus'
    last_name = 'Wagner'
    team_name = 'Pittsburgh'
    hof = False
    portrait = False
    horizontal = False

    @classmethod
    def _setup_next_sequence(cls):
        return 1
