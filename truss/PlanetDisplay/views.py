from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Planet
import requests, json

# Create your views here.
def index(request):
    # Curl
    try:
        url = 'https://swapi.dev/api/planets/?format=json'
        r = requests.get(url).json()['results']
        planet_list = []
        for result in r:
            if result['name'] != 'unknown':
                p_name = result['name']
            else:
                p_name = '?'

            if result['climate'] != 'unknown':
                p_climate = result['climate']
            else:
                p_climate = '?'

            if result['residents']:
                p_residents = len(result['residents'])
            else:
                p_residents = 0

            if result['climate'] != 'unknown':
                p_climate = result['climate']
            else:
                p_climate = '?'

            if result['terrain'] != 'unknown':
                p_terrain = result['terrain']
            else:
                p_terrain = '?'

            if result['population'] != 'unknown':
                p_population = result['population']
            else:
                p_population = '?'

            if result['surface_water'] != 'unknown' and result['diameter'] != 'unknown':
                p_surface_water = round((int(result['surface_water'])/100) * int(result['diameter']))
            else:
                p_surface_water = '?'

            planet_list.append(
                    Planet(
                        name=p_name, 
                        climate=p_climate, 
                        population=p_population, 
                        residents=p_residents,
                        surface_water=p_surface_water, 
                        terrain=p_terrain, 
                        url=result['url']
                    )
            )
    
        template = loader.get_template('PlanetDisplay/index.html')
        context = {
            'planets': planet_list,
        }
        return HttpResponse(template.render(context, request))
    except:
        return HttpResponse("Invalid url, cannot find data")