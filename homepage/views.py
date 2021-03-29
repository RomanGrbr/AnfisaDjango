from django.shortcuts import render
from icecream.models import icecream_db

# def index(request):
#     return render(request, 'homepage/index.html')

def index(request):
    icecreams = ''
    for i in range(len(icecream_db)):
        # Измените строку, добавляемую к icecreams
        icecreams += f"{icecream_db[i]['name']} | <a href='icecream/{i}/'>Узнать состав</a><br>"
    context = {
        'icecreams': icecreams,
    }
    return render(request, 'homepage/index.html', context)