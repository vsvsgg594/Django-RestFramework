from django.shortcuts import render
from .models import Staff
from .serializer import StaffSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class StaffApi(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
    authentication_classes=[BaseAuthentication]
    pagination_class=[IsAuthenticated]
