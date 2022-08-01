from django.db import models
from django_celery_results.models import TaskResult

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200,blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)

class Celery_Result(models.Model):
    celery = models.ForeignKey(TaskResult, on_delete=models.CASCADE)
    shown = models.BooleanField(default=False)