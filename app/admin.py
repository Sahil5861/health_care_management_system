from django.contrib import admin
from .models import Appointment, Healthchceck, Specialist

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Healthchceck)
admin.site.register(Specialist)

