from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(Diagnosis)
admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(Article)