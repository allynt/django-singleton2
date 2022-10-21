import pytest

from django.core.exceptions import ValidationError

from example.tests.factories import *


@pytest.mark.django_db
class TestSingleton:

    def test_singleton_cannot_create_multiple(self):
        """
        Test that a singleton can only be created once.
        """
        singleton_1 = ExampleSingletonModelFactory()
        singleton_2 = ExampleSingletonModelFactory()
        singleton_1.save()
        singleton_2.save()
        assert singleton_1.pk is not None
        assert singleton_2.pk is None
        assert ExampleSingletonModel.objects.count() == 1

    def test_singleton_raises_error(self, settings):
        """
        Test that when a user tries to create multiple singletons,
        it raises an exception if SINGLETON_RAISE_ERROR_ON_SAVE is True.
        """

        settings.SINGLETON_RAISE_ERROR_ON_SAVE = True

        with pytest.raises(ValidationError):
            singleton_1 = ExampleSingletonModelFactory()
            singleton_2 = ExampleSingletonModelFactory()
