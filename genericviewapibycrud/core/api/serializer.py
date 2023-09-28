from .models import CustomerDetail
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerDetail
        fields=['id','name','role','city']