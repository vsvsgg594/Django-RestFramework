from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Emp
from .serializer import EmpSerilizer

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def emp_api(request,pk=None):
    if request.method=="GET":
        id=request.data.get('id')

        if id is not None:
            emp=Emp.objects.get(id=id)
            serializer=EmpSerilizer(emp)
            return Response(serializer.data)
        emp=Emp.objects.all()
        serializer=EmpSerilizer(emp,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=EmpSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data created"})
        return Response(serializer.errors)
    if request.method=="PUT":
        id=pk
        emp=Emp.objects.get(pk=id)
        serializer=EmpSerilizer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data update"})
        return Response(serializer.errors)
    if request.method=="DELETE":
        id=pk
        emp=Emp.objects.get(id=id)
        emp.delete()
        return Response({"msg":"data deleted"})
    return Response({"msg":"data canot fount"})

