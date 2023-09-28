from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from api.models import Company
from api.serilizer import CompanySerilizer
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerilizer
