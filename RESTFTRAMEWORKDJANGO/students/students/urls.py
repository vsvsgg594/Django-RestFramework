"""
URL configuration for students project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from api2 import views as v
from app3 import views as v3

urlpatterns = [
    path("admin/", admin.site.urls),
    path('stdinfo/',views.students_detail),
    path('stdlist/',views.students_list),
    path('stdcreate/',v.student_create),
    path('empdata/',v3.emp_serializer),

]
