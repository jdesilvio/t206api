"""Base factory."""

import factory


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base factory."""

    id = factory.Sequence(lambda n: n)

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    # TODO: Can the session.commit() be generalized?
#    @classmethod
#    def _create(cls, model_class, *args, **kwargs):
#        obj = model_class(*args, **kwargs)
#        obj.save()
#        return obj
