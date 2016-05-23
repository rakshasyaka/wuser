from django.contrib import admin

from .models import Event, Update, Rule

admin.site.register(Event)
admin.site.register(Rule)
admin.site.register(Update)
