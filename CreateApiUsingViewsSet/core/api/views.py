from django.shortcuts import render
from .serializer import EmpSerializer
from .models import Employee
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        emp=Employee.objects.all()
        serializer=EmpSerializer(emp,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmpSerializer(emp)
            return Response(serializer.data)
    def create(self,request):
        serializer=EmpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'data created'})
        return Response(serializer.errors)
    def destroyed(self ,request,pk):
        id=pk
        emp=Employee.objects.get(id=id)
        emp.delete()
        return Response({'msg':'data deletd'})    
 


       