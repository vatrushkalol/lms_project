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
from .signals import account_access


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

        # Send email about autorization
        account_access.send(sender=self.__class__, request=self.request)

        return super(UserLoginView, self).form_valid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')



def log_out(request):
    logout(request)
    return redirect('login')

