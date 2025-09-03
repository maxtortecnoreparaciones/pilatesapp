from django.db import models
from usuarios.models import Usuario
from clases.models import Clase

class EtiquetaProgreso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre

class ProgresoAlumno(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='progresos')
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='progresos')
    etiqueta = models.ForeignKey(EtiquetaProgreso, on_delete=models.CASCADE, related_name='progresos')
    fecha_asignacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.alumno.nombre} - {self.etiqueta.nombre}'