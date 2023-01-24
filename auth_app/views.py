from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse('<div><h1><b>Здесь находится страница входа пользователя на сайт</b></h1></div>')

def register(request):
    return HttpResponse('<div><h1><b>Здесь находится страница регистрации пользователя</b></h1></div>')

def logout(request):
    return HttpResponse('<div><h1><b>Здесь находится страница выхода из учетной записи и переход на главную страницу</b></h1></div>')

def change_password(request):
    return HttpResponse('<div><h1><b>Здесь находится страница смены пароля пользователя</b></h1></div>')

def reset_password(request):
    return HttpResponse('<div><h1><b>Здесь находится страница восстановления пароля</b></h1></div>')

