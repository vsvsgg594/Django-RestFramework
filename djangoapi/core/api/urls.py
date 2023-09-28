from api.views import CompanyViewSet
from django.urls import path,include
from rest_framework import routers
from rest_framework import viewsets



router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)

urlpatterns = [
   path('',include(router.urls)),
]
