from django.db import models
from django.db.models import Model, CharField


# Create your models here.
class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"
