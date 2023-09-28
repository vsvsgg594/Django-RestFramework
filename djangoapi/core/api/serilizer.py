from rest_framework import serializers
from api.models import Company
from django.core import serializers
from .serialize import *

class CompanySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Company
        field="__all__"
