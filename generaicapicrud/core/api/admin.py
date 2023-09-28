from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_display=['id','name','role','city']
