from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class Planet(models.Model):
    climate = models.CharField(max_length=200)
    diameter = models.IntegerField()
    gravity = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    orbital_period = models.IntegerField()
    population = models.IntegerField()
    residents = ListCharField(
        base_field=models.CharField(max_length=100),
        size=20,
        max_length=(20*101),
    )
    rotation_period = models.IntegerField()
    surface_water = models.IntegerField()
    terrain = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
