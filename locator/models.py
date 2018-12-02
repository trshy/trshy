from django.db import models

# Create your models here.


class Trashcan(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    full_rating = models.IntegerField(default=0)
    missing_rating = models.IntegerField(default=0)
