from django.shortcuts import render
from .models import CustomerDetail
from .serializer import CustomerSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin

# Create your views here.

class CustomerDetailApi(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=CustomerDetail.objects.all()
    serializer_class=CustomerSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
