from django.http import HttpResponse
from . import models

def icecream_list(request):
    db_query = models.icecream_db
    icecreams = f'Список мороженого: {db_query}'
    return HttpResponse(icecreams)