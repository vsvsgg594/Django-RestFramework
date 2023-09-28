from django.shortcuts import render
from rest_framework.views import APIView
from .models import StudentModel
from .serializer import StudentSerialzer
from rest_framework.response import Response

# Create your views here.

class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=StudentModel.objects.get(id=id)
            serializer=StudentSerialzer(stu)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        stu=StudentModel.objects.all()
        serializer=StudentSerialzer(stu,many=True)

        return Response(serializer.data)
    def post(self,request,format=None):
        serializer=StudentSerialzer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    def put(self,request,pk=None,format=None):
        id=pk
        stu=StudentModel.objects.get(pk=id)
        serializer=StudentSerialzer(stu,request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'updated'})
        return Response(serializer.errors)
    def delete(self,request,pk=None,format=None):
        id=pk
        stu=StudentModel.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data delete'})
    
        
           