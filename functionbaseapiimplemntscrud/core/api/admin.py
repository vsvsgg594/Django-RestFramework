from django.contrib import admin
from .models import     Studentss

# Register your models here.
@admin.register(Studentss)

class StudentsModel(admin.ModelAdmin):
    list_display=['id','name','roll','city']
