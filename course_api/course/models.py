from django.db import models
from django.db.models.fields import CharField

class Course(models.Model):
    name = CharField(max_length=200)
    language = CharField(max_length=100)
    price = CharField(max_length=10)

    def __str__(self):
        return self.name