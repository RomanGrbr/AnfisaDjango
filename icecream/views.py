from . import models
from django.shortcuts import render

def icecream_list(request):
    icecreams = ''
    for i in range(len(models.icecream_db)):
        icecreams += f'{models.icecream_db[i]["name"]} <br>'
    context = {'icecreams': icecreams,}
    return render(request, 'icecream/icecream-list.html', context)