from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Studentss
from .serializer import StudentsSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])

def students_api(request,pk=None):
    if request.method=="GET":
        id=request.data.get('id')
        if id is not None:
            stu=Studentss.objects.get(id=id)
            serializer=StudentsSerializer(stu)
            return Response(serializer.data)
        stu=Studentss.objects.all()
        serializer=StudentsSerializer(stu,many=True)
        return Response(serializer.data)    
    if request.method=="POST":
        data=request.data
        serializer=StudentsSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    if request.method=="PUT":
        id=pk
        stu=Studentss.objects.get(pk=id)
        serializer=StudentsSerializer(stu,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data update'})
        return Response(serializer.errors)
    if request.method=="DELETE":
        id=pk
        stu=Studentss.objects.get(pk=id)
        stu.delete()
        return Response({'mgs':'data delete'})
    


