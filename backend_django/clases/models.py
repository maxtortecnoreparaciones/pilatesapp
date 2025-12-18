from django.db import models
from usuarios.models import Usuario
from sedes.models import Sede

class Clase(models.Model):
    """
    Modelo que representa una clase agendable en una sede, impartida por un profesor.
    """
    sede = models.ForeignKey('sedes.Sede', on_delete=models.CASCADE, related_name='clases')
    profesor = models.ForeignKey('usuarios.Usuario', on_delete=models.PROTECT, related_name='clases_impartidas')
    tipo_disciplina = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    cupos_totales = models.IntegerField()
    cupos_disponibles = models.IntegerField()

    class Meta:
        ordering = ['fecha_hora']
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return f"{self.tipo_disciplina} - {self.sede.nombre} ({self.fecha_hora:%d/%m/%Y %H:%M})"

class Agendamiento(models.Model):
    ESTADOS_AGENDAMIENTO = [
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado'),
        ('Asistió', 'Asistió'),
        ('No asistió', 'No asistió'),
    ]
    alumno = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='agendamientos')
    clase = models.ForeignKey('clases.Clase', on_delete=models.CASCADE, related_name='agendamientos')
    fecha_agendamiento = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_AGENDAMIENTO, default='Confirmado')

    def __str__(self):
        return f'{self.alumno.nombre_completo} agendó {self.clase.tipo_disciplina}'