from django.db import models

# Create your models here.

class Student(models.Model):
    studentId=models.IntegerField()
    studentName=models.CharField(max_length=100)
    studentAddress=models.CharField(max_length=100)
