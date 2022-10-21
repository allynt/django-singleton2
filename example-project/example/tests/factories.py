import factory

from example.models import ExampleSingletonModel


class ExampleSingletonModelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ExampleSingletonModel

    name = factory.Faker("word")
