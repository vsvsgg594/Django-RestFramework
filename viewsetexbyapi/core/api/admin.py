from django.contrib import admin
from .models import Teacher

# Register your models here
# .
@admin.register(Teacher)
class TeacherAdminModel(admin.ModelAdmin):
    list_display=['id','name','role','salary']
