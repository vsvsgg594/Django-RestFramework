from django.db import models

# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    position=models.CharField(max_length=100)