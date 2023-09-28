from django.shortcuts import render
from .models import Emp
from .serializer import EmpModelSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.


def emp_serializer(request):
    emp_obj=Emp.objects.all()
    serializer_obj=EmpModelSerializer(emp_obj,many=True)
    json_data=JSONRenderer().render(serializer_obj.data)

    return HttpResponse(json_data,content_type='application/json')


