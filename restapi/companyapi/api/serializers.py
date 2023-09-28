from rest_framework import serializers
from api.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    
    class Meta:
        model=Company
        field={'name':'name','locations':'location','about':'about','type':'type'}
        