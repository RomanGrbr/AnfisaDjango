from django.http import HttpResponse


def icecream_list(request):
    return HttpResponse('Здесь будет список сортов мороженого')