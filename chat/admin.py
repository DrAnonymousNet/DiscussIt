import django
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Message)
admin.site.register(Event)
admin.site.register(Group)
