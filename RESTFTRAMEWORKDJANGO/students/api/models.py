from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    locations=models.CharField(max_length=100)



