"""Card factory."""

import factory

from t206api.models import Card  # noqa: I202

from . import Session


class CardFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Card factory."""

    class Meta:  # pylint: disable=no-init,old-style-class
        """Card factory meta options."""

        model = Card
        sqlalchemy_session = Session

    id = factory.Sequence(lambda n: n)
    first_name = 'Honus'
    last_name = 'Wagner'
    variety = factory.Sequence(lambda n: 'Variety {}'.format(n))

    @classmethod
    def _setup_next_sequence(cls):
        return 1
