from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Account)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Symptom)
admin.site.register(Disease)