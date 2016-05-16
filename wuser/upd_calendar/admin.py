from django.contrib import admin

from .models import Event, Update

admin.site.register(Event)
admin.site.register(Update)