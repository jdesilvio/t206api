"""Factory factory."""

import factory
import factory.fuzzy

from t206api.models import Factory  # noqa: I202
from t206api.models.factory import district_types, state_types

from . import Session


class FactoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Factory factory."""

    class Meta:  # pylint: disable=no-init
        """Factory factory meta options."""

        model = Factory
        sqlalchemy_session = Session

    id = factory.Sequence(lambda n: n)
    number = factory.fuzzy.FuzzyInteger(1, 42)
    district = factory.Faker('word', ext_word_list=district_types)
    state = factory.Faker('word', ext_word_list=state_types)
