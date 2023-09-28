from django.contrib import admin
from .models import Company
@admin.register(Company)

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','location','type']