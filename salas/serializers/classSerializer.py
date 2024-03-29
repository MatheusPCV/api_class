from rest_framework import serializers
from ..models.classEntity import salaEntity

class classSerializer(serializers.Serializer):
    numero = serializers.IntegerField( max_lenght=3)
    capacidade = serializers.IntegerField(max_lenght=4)