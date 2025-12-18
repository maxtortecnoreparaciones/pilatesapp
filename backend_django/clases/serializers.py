from rest_framework import serializers
from .models import Clase, Agendamiento

class ClaseSerializer(serializers.ModelSerializer):
    sede_nombre = serializers.CharField(source='sede.nombre', read_only=True)
    class Meta:
        model = Clase
        fields = ['id', 'tipo_disciplina', 'fecha_hora', 'cupos_totales', 'cupos_disponibles', 'sede', 'sede_nombre']

class AgendamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamiento
        fields = '__all__'