# pilates/serializers.py

from rest_framework import serializers
from .models import Usuario, Sede, Clase, Agendamiento, Notificacion, Pago, EtiquetaProgreso, ProgresoAlumno, RegistroAcceso, Referido

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nombre', 'rol', 'nivel_alumno', 'numero_telefono']

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class ClaseSerializer(serializers.ModelSerializer):
    profesor_nombre = serializers.ReadOnlyField(source='profesor.nombre')
    sede_nombre = serializers.ReadOnlyField(source='sede.nombre')
    
    class Meta:
        model = Clase
        fields = ['id', 'profesor', 'profesor_nombre', 'disciplina', 'tipo_clase', 'fecha_hora_inicio', 'duracion_minutos', 'cupos_totales', 'cupos_disponibles', 'sede', 'sede_nombre', 'precio', 'estado']

class AgendamientoSerializer(serializers.ModelSerializer):
    alumno_nombre = serializers.ReadOnlyField(source='alumno.nombre')
    clase_disciplina = serializers.ReadOnlyField(source='clase.disciplina')
    clase_fecha = serializers.DateTimeField(source='clase.fecha_hora_inicio', read_only=True)

    class Meta:
        model = Agendamiento
        fields = ['id', 'alumno', 'alumno_nombre', 'clase', 'clase_disciplina', 'clase_fecha', 'fecha_agendamiento', 'estado']
        
class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class EtiquetaProgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtiquetaProgreso
        fields = '__all__'

class ProgresoAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoAlumno
        fields = '__all__'

class RegistroAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAcceso
        fields = '__all__'

class ReferidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referido
        fields = '__all__'