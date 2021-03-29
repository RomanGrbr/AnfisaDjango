from django.shortcuts import render
from icecream.models import icecream_db
from anfisafriends.models import friends_db


def index(request):
    icecreams = ''
    friends = ''
    for i in friends_db:
        friends += f"{i}<br>"

    for i in range(len(icecream_db)):
        icecreams += f"{icecream_db[i]['name']} | <a href='icecream/{i}/'>Узнать состав</a><br>"
    context = {
        'icecreams': icecreams,
        'friends': friends,
    }
    return render(request, 'homepage/index.html', context)