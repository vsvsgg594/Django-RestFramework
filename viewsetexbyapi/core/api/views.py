from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Teacher
from .serializer import TeacherModelSerializer
# Create your views here.

class TeacherApi(viewsets.ViewSet):

    def list(self,request):
        t=Teacher.objects.all()
        serializer=TeacherModelSerializer(t,many=True)

        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not  None:
            t=Teacher.objects.get(id=id)
            serialzer=TeacherModelSerializer(t)
            return Response(serialzer.data)
        
    def create(self,request):
        serializer=TeacherModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'data created'})  
        return Response(serializer.errors)  
    def destroy(self,request,pk=None):
        id=pk
        t=Teacher.objects.get(id=id)
        t.delete()
        return Response({'msg':'data deletes'})
