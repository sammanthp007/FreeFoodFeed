from django.contrib import admin
from .models import PersonType, EventType

# Register your models here.

admin.site.register(PersonType)
admin.site.register(EventType)