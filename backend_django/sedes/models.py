from django.db import models

class Sede(models.Model):
    """
    Modelo que representa una ubicación física (Sede) asociada a un Estudio (Tenant).
    El nombre de la sede es único dentro de cada estudio.
    """
    estudio = models.ForeignKey('estudios.Estudio', on_delete=models.CASCADE, related_name='sedes')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    class Meta:
        unique_together = ('estudio', 'nombre')
        ordering = ['estudio__nombre', 'nombre']
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return f"{self.nombre} ({self.estudio.nombre})"