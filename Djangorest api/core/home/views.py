
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialize import TodoSerialier
from .models import Todo
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    if request.method=='GET':
        return Response({
                 'status':400,
                'message':"hello this is api",
                'methode_called' :"this is get methodes",


             })
    elif request.method=='POST':
        return Response({
            'status':405,
            'message':"this is api called",
            'method_call':'this is post method',
        })
    else:
        return Response({
            'method_call':'invalied',
        })
@api_view(['POST'])     
def post_todo(request):
    try:
        data=request.data
        serializer=TodoSerialier(data=data)
        if serializer.is_valid():
            print(serializer.data)
        print(data)
        return Response({
            'status':True,
            'method_call':'valied',
        })

    except Exception as e:

        print(e)  
    return Response({
             'status':False, 
            'method_call':'invalied',
        })   
@api_view(['GET'])
def get_todo(request):
    todo_objs=Todo.objects.all()
    seriliers=TodoSerialier(todo_objs,many=True)   




    return Response({
        'status':123,
        'message':'todo fetch',
        'data':seriliers.data
    })



            
        

   
