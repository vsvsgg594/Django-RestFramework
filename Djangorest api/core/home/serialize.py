from rest_framework import serializers
from .models import Todo
from .serialize import *


class TodoSerialier(serializers.ModelSerializer):

    class Meta:
        model=Todo
        fields=['todo_title']