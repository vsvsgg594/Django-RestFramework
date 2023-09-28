from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def students_detail(request):
    stud=Students.objects.get(id=1)
    serializer=StudentsSerializer(stud)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def students_list(request):
    stud=Students.objects.all()
    serializer=StudentsSerializer(stud,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')



