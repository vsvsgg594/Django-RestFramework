from django.contrib import admin
from .models import Emp

# Register your models here.
@admin.register(Emp)

class EmpModel(admin.ModelAdmin):
    list_display=['id','empName','empId','empCity']
