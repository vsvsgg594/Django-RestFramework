from django.shortcuts import render

# Create your views here.
def home(request):
    person=[{'name':'vikash','age':23},{'name':'vikash','age':23}]
    for persons in person:
        print(persons)
    return render(request ,"index.html",context={'person':person})  
def number(request):
    list=[1,2,3,4,5,6]
    for lists in list:
        print(lists)
    return render(request , "index.html", context={'list':list})      
