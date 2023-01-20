from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(User)
admin.site.unregister(Group)
admin.site.site_header = 'Learning Management System'