
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

routers=DefaultRouter()

routers.register('teacherApi',views.TeacherApi,basename='teacher')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(routers.urls)),
]
