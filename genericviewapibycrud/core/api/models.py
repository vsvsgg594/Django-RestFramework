from django.db import models

# Create your models here.

class CustomerDetail(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    city=models.CharField(max_length=100)