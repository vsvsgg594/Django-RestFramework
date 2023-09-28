from rest_framework import serializers
from .models import Emp

class EmpSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields=['id','empName','empId','empCity']
