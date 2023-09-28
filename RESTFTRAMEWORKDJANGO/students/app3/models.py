from django.db import models

# Create your models here.

class Emp(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=100)
    emp_location=models.CharField(max_length=100)
