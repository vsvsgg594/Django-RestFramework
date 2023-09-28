from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentssModelserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=="POST":
        jsno_data=request.body
        stream=io.BytesIO(jsno_data)
        pythondata=JSONParser().parse(stream)

        serializer=StudentssModelserializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()

            res={'msg':'data created !'} 
            jsno_data=JSONRenderer.render(res)

            return HttpResponse(jsno_data,content_type='application/json')


         
