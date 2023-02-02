from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from .models import User


# Create your views here.

def log_in(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Ваш аккаунт заблокирован')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        data = request.POST
        user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'],
                    description=data['description'], birthday=data['birthday'], avatar=data['avatar'])
        user.set_password(data['password'])
        user.save()
        login(request, user)
        return redirect('index.html')
    else:
        return render(request, 'register.html')


def log_out(request):
    logout(request)
    return redirect('login')


def change_password(request):
    return HttpResponse('<div><h1><b>Здесь находится страница смены пароля пользователя</b></h1></div>')


def reset_password(request):
    return HttpResponse('<div><h1><b>Здесь находится страница восстановления пароля</b></h1></div>')


