from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# @api_view(['GET'])
# def hellow_word(request):
#     return Response({'msg':'hello world !'})



# @api_view(['POST'])
# def post_data(request):
#     if request.method=="POST":

#         return Response({'msg':'post methiod'})
    

@api_view(['GET','POST'])

def methods(request):
    if request.method=="GET":
        print(request.data)
        return Response({'msg':'get methods'})
    elif request.method=="POST":
        print(request.data)
        return Response({'msg':'post methods','data':request.data})
    else:
        return Response({'msg':"incvalied request"})