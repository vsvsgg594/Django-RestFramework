from rest_framework import serializers
from .models import StudentModel

class StudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=['id','name','roll','city']
