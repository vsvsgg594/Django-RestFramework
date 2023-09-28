from rest_framework import serializers
from .models import Studentss

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Studentss
        fields=['id','name','roll','city']
