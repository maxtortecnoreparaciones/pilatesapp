from django.db import models
from usuarios.models import Usuario

class Notificacion(models.Model):
    TIPOS = [
        ('Enviado', 'Enviado'),
        ('Recibido', 'Recibido'),
    ]
    ESTADOS = [
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
        ('Leído', 'Leído'),
        ('Error', 'Error'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones')
    contenido = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPOS)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='Enviado')

    def __str__(self):
        return f"{self.tipo} - {self.usuario.email}"