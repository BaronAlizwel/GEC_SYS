from django.contrib import admin
from events.models import Attendance, Event, EventType

# Register your models here.

admin.site.register(Attendance)
admin.site.register(EventType)
admin.site.register(Event)
