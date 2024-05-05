from django.db import models

from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Memory(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.TextField()
