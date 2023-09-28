from django.shortcuts import render
from .models import Laptop
from .serializer import LaptopSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.
def listDetail(request):
    lap=Laptop.objects.get(id=1)
    serializer=LaptopSerializer(lap)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def allData(request):
    lap=Laptop.objects.all()
    serializer=LaptopSerializer(lap,many=True)
    json_data=JSONRenderer().render(serializer.data)

    return HttpResponse(json_data,content_type='application/json')
