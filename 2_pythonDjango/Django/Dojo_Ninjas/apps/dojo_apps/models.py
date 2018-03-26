from __future__ import unicode_literals
from django.db import models


class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        Dojos.objects.create(name="CodingDojo New York", city="New York", state="NY")
        return "{} {} {} {}".format(self.name, self.city, self.state, self.created_at, self.updated_at)

# Create your models here.


class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        Ninjas.objects.create(first_name="CodingDojo New York", last_name="New York")
        return "{} {} {} {}".format(self.dojo, self.first_name, self.last_name, self.created_at, self.updated_at)