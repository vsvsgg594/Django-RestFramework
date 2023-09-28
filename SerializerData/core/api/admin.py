from django.contrib import admin
from .models import Laptop

# Register your models here.
@admin.register(Laptop)
class LaptopAdminModel(admin.ModelAdmin):
    list_display=['id','name','modelNo','price']
