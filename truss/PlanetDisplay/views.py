from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Planet
import requests, json

# Create your views here.
def index(request):
    # Curl
    url = 'https://swapi.dev/api/planets/?format=json'
    r = requests.get(url).json()['results']
    planet_list = []
    for result in r:
        planet_list.append(
                Planet(
                        name=result['name'], 
                        diameter=result['diameter'], 
                        gravity=result['gravity'], 
                        climate=result['climate'], 
                        orbital_period=result['orbital_period'], 
                        population=result['population'], 
                        residents=result['residents'],
                        rotation_period=result['rotation_period'], 
                        surface_water=result['surface_water'], 
                        terrain=result['terrain'], 
                        url=result['url']
                    )
            )
    
    template = loader.get_template('PlanetDisplay/index.html')
    context = {
        'planets': planet_list,
    }
    return HttpResponse(template.render(context, request))