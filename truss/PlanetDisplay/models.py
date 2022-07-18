from django.db import models

# Create your models here.
class Planet(models.Model):
    climate = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    population = models.IntegerField()
    residents = models.IntegerField()
    surface_water = models.IntegerField()
    terrain = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
