from django.db import models
from usuarios.models import Usuario
from sedes.models import Sede

class Clase(models.Model):
    TIPOS_CLASE = [
        ('Semi-personalizada', 'Semi-personalizada'),
        ('A domicilio', 'A domicilio'),
        ('Virtual', 'Virtual'),
    ]
    ESTADOS_CLASE = [
        ('Programada', 'Programada'),
        ('Cancelada', 'Cancelada'),
        ('Completada', 'Completada'),
    ]
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='clases_impartidas')
    disciplina = models.CharField(max_length=100)
    tipo_clase = models.CharField(max_length=20, choices=TIPOS_CLASE)
    fecha_hora_inicio = models.DateTimeField()
    duracion_minutos = models.PositiveIntegerField()
    cupos_totales = models.PositiveIntegerField()
    cupos_disponibles = models.PositiveIntegerField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='clases')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS_CLASE, default='Programada')

    def __str__(self):
        return f'{self.disciplina} en {self.sede.nombre}'

class Agendamiento(models.Model):
    ESTADOS_AGENDAMIENTO = [
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado'),
        ('Asistió', 'Asistió'),
        ('No asistió', 'No asistió'),
    ]
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='agendamientos')
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='agendamientos')
    fecha_agendamiento = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_AGENDAMIENTO, default='Confirmado')

    def __str__(self):
        return f'{self.alumno.nombre} agendó {self.clase.disciplina}'