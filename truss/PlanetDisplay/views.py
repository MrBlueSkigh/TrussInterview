from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Planet

# Create your views here.
def index(request):
    # Curl
    url = 'https://swapi.dev/api/planets/'

    p = Planet(climate = "yes", diameter = 1, gravity = "yes", name = "yes", orbital_period = 1, population = 1, residents = ["mike", "billy"], rotation_period = 1, surface_water = 1, terrain = "yes", url = "yes")
    planet_list = [p]
    template = loader.get_template('PlanetDisplay/index.html')
    context = {
        'planets': planet_list,
    }
    return HttpResponse(template.render(context, request))