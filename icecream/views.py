from django.http import HttpResponse
from . import models

def icecream_list(response):
    icecreams = ''
    for i in range(len(models.icecream_db)):
        icecreams += f'{models.icecream_db[i]["name"]} :: '
    return HttpResponse(f'Список сортов мороженого: {icecreams}')