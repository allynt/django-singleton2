from django.db import models

from singleton2.models import SingletonMixin


class ExampleSingletonModel(SingletonMixin, models.Model):

    class Meta:
        verbose_name = "Example Singleton"
        verbose_name_plural = "Example Singletons"

    name = models.CharField(unique=True, max_length=128)

    def __str__(self) -> str:
        return self.name
