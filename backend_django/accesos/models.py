from django.db import models
from usuarios.models import Usuario
from sedes.models import Sede

class RegistroAcceso(models.Model):
    RESULTADOS = [
        ('Exitoso', 'Exitoso'),
        ('Fallido', 'Fallido'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='registros_acceso')
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='registros_acceso')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=10, choices=RESULTADOS)

    def __str__(self):
        return f'{self.usuario.nombre} - {self.resultado}'