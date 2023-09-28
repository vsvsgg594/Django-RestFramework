from rest_framework import serializers
from .models import Teacher

class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"