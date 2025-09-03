from django.db import models
from usuarios.models import Usuario

class Referido(models.Model):
    codigo_referido = models.CharField(max_length=50, unique=True)
    referidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='referidos_creados')
    referido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='referidos_usados', null=True, blank=True)
    fecha_uso = models.DateTimeField(null=True, blank=True)
    recompensa_otorgada = models.BooleanField(default=False)

    def __str__(self):
        return f'Código: {self.codigo_referido}'