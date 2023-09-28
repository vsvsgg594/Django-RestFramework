from django.contrib import admin
from .models import Staff

# Register your models here.
@admin.register(Staff)
class StaffAminModel(admin.ModelAdmin):
    list_display=['id','name','salary','position']
