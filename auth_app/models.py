from django.db import models
from django.contrib.auth.models import AbstractUser
from .functions import get_timestamp_path_user


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=False)
    username = models.TextField(verbose_name='Логин', null=True, blank=True, max_length=20)
    description = models.TextField(verbose_name='Обо мне', null=True, blank=True, default='', max_length=150)
    avatar = models.ImageField(verbose_name='Аватар', blank=True, upload_to=get_timestamp_path_user)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = 'Участники'
        verbose_name = 'Участник'
        ordering = ['last_name']

    def __str__(self):
        return f'Участник {self.first_name} {self.last_name}: {self.email}`'
# Create your models here.


