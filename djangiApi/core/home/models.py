from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
class Number(models.Model):

    number=models.IntegerField()   
