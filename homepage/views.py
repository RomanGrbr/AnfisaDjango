import sys
from django.shortcuts import render
from icecream.models import icecream_db
from anfisafriends.models import friends_db
from anfisafriends.services import what_weather


def index(request):
    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''

    for friend in friends_db:
        friends += (f'<input type="radio" name="friend"'
                    f'required value="{friend}">{friend}<br>')

    for i in range(len(icecream_db)):
        icecreams += (f'{icecream_db[i]["name"]} | '
                      f'<a href="icecream/{i}/">Узнать состав</a><br>')

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        city = friends_db[selected_friend]
        weather = what_weather(city)
        friend_output = f'{selected_friend}, тебе прислали мороженое!'
        city_weather = f'Погода в городе {city}: {weather}'

        print(f'имя друга: {selected_friend} \n'
              f'город: {city} \n'
              f'погода в городе: {weather} \n'
              f'текст для вывода: {friend_output} \n'
              f'погода для вывода: {city_weather} \n',
              file=sys.stderr)

    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,

    }
    return render(request, 'homepage/index.html', context)
