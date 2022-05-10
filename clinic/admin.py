from django.contrib import admin

from .models import Disease, Symptom, Reason, Treatment,Speciality

# Register your models here.
admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(Reason)
admin.site.register(Treatment)
admin.site.register(Speciality)