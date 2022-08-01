from django.contrib import admin
from app.models import Person, Celery_Result

# Register your models here.

admin.site.register(Person)
admin.site.register(Celery_Result)