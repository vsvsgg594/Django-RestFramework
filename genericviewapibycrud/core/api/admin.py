from django.contrib import admin
from .models import  CustomerDetail

# Register your models here.
@admin.register(CustomerDetail)
class CustomerAdminModel(admin.ModelAdmin):
    list_display=['id','name','role','city']
