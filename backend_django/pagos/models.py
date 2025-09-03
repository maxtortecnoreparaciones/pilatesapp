from django.db import models
from usuarios.models import Usuario
from clases.models import Agendamiento

class Pago(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Fallido', 'Fallido'),
    ]
    agendamiento = models.ForeignKey(Agendamiento, on_delete=models.SET_NULL, null=True, blank=True, related_name='pagos')
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='Pendiente')
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f'Pago de {self.monto} por {self.alumno.nombre}'