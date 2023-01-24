from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<div><h1><b>Главная страница с курсами</b></h1></div>')

def create(request):
    return HttpResponse('<div><h1><b>Здесь находится страница для создания курса</b></h1></div>')

def delete(request, course_id):
    return HttpResponse(f'<div><h1><b>Здесь находится страница удаление {course_id} курса</b></h1></div>')

def detail(request, title):
    return HttpResponse(f'<div><h1><b>Здесь находится страница описания {title} курса</b></h1></div>')

def enroll(request, title):
    return HttpResponse(f'<div><h1><b>Здесь находится страница записи на курс {title}</b></h1></div>')



