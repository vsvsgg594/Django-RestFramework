from django.contrib import admin
from .models import StudentsModel
# Register your models here.
@admin.register(StudentsModel)
class StudentsModelAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
