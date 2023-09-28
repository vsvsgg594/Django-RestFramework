from django.db import models

# Create your models here.
class Emp(models.Model):
    empName=models.CharField(max_length=100)
    empId=models.IntegerField()
    empCity=models.CharField(max_length=100)