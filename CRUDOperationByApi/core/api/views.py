from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def students_api(request):
    if request.method=='GET':
        jsno_data=request.body
        stream=io.ByteIO(jsno_data)
        pythondata=JSONParser().parse(stream)

        id=pythondata.get('id',None)

        if id is not None:
            stu=Student.objects.get(id=id)

            serializer=StudentSerializer(stu)

            jsno_data=JSONRenderer().render(serializer.data)

            return HttpResponse(jsno_data,content_type='application/json')
        stu=Student.objects.all()
        serilizer=StudentSerializer(stu,many=True)
        jsno_data=JSONRenderer().render(serializer.data)

        return HttpResponse(jsno_data,content_type='application/json')

