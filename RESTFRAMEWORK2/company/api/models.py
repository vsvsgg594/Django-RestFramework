from django.db import models

# Create your models here.
TYPE=(('IT','IT'),('Non-IT','Non-IT'))

class Company(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=TYPE)
    added_date=models.DateTimeField(auto_now_add=True)
    active=models.DateField(auto_now=True)
