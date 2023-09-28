from rest_framework import serializers


class StudentsSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    locations=serializers.CharField(max_length=100)





