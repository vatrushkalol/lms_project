from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    re_path('^delete/(?P<course_id>[1-9]*)/$', delete, name='delete'),
    path('detail/<str:title>/', detail, name='detail'),
    path('enroll/<str:title>/', enroll, name='enroll')
]