from django.urls import path
from .views import *

urlpatterns = [
    path('get-todo/',get_todo,name="get_todo"),
    path('', home, name="home"),
    path('post-todo/', post_todo , name="post_todo"),
    
]