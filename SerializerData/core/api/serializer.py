from rest_framework import serializers
from .models import Laptop

class LaptopSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    modelNo=serializers.CharField(max_length=100)
    price=serializers.FloatField()
    
