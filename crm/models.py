from django.db import models

# Create your models here.
class Employeemodel(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=40)
    place = models.CharField(max_length=50)
    salary = models.IntegerField()