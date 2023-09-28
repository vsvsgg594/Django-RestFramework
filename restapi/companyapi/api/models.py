from django.db import models

# Create your models here.
#creating company models
TYPE=(('IT','IT'),('NON-IT','NON-IT'))

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    locations=models.CharField(max_length=100)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=TYPE)
    added_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
