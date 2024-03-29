from rest_framework import serializers
from ..models import reserveEntity

class ReserveEntitySerializer(serializers.Serializer):
    nome_professor = serializers.CharField()
    materia = serializers.CharField()
    inicio_reserva = serializers.DateTimeField()
    fim_reserva = serializers.DateTimeField()