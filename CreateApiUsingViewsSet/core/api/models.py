from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    companyName=models.CharField(max_length=100)
    salary=models.IntegerField()
