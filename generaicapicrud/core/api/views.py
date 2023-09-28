from django.shortcuts import render
from .models import Customer
from .serializer import CustomerSeroializer
from rest_framework.generics import  GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
# Create your views here.

class CustomerApi(GenericAPIView,ListModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSeroializer

    def get(self,request,*args,**kwargs):

        return self.list(request,*args,**kwargs)
    

class CustomerCreateApi(GenericAPIView,CreateModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSeroializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class CustomerRetrive(GenericAPIView,RetrieveModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSeroializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)   

class CustomerDestroyed(GenericAPIView,DestroyModelMixin):
    queryset=Customer.objects.all()
    serializer_class=CustomerSeroializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)         
