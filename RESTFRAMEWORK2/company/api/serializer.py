from rest_framework import serializers
from .models import Company



class CompanySerializer(serializers.HyperlinkedModelSerializer):
    name=serializers.CharField(max_length=100)
    location=serializers.CharField(max_length=100)
  
    
    class Meta:
        model=Company
       