from django.shortcuts import render


def index(request):
    return render(request, 'home.html', context={'title': 'Портал ААА - Главная',})