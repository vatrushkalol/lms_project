from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from datetime import datetime
from .models import User
from django.views.generic.edit import CreateView
from .forms import LoginForm, RegisterForm


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    next_page = 'index'

    def form_valid(self, form):
        is_remeber = self.request.POST.get('is_remember')
        if is_remeber == 'on':
            self.request.session[settings.REMEMBER_KEY] = datetime.now().isoformat()
            self.request.session.set_expiry(settings.REMEMBER_AGE)
        elif is_remeber == 'off':
            self.request.session.set_expiry(0)
        return super(UserLoginView, self).form_valid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        pupil = Group.objects.filter(name='Ученик')
        user.groups.set(pupil)
        login(self.request, user)
        return redirect('index')



def log_out(request):
    logout(request)
    return redirect('login')


def change_password(request):
    return HttpResponse('<div><h1><b>Здесь находится страница смены пароля пользователя</b></h1></div>')


def reset_password(request):
    return HttpResponse('<div><h1><b>Здесь находится страница восстановления пароля</b></h1></div>')


