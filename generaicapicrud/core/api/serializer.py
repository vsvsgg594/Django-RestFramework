from rest_framework import serializers
from .models import Customer

class CustomerSeroializer(serializers.ModelSerializer):

    class Meta:
        model=Customer
        fields=['id','name','role','city']