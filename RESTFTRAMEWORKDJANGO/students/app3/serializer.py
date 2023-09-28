from rest_framework import serializers
from .models import Emp


class EmpModelSerializer(serializers.Serializer):
    emp_id=serializers.IntegerField()
    emp_name=serializers.CharField(max_length=100)
    emp_location=serializers.CharField(max_length=100)
     
