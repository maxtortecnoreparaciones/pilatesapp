# Contenido de C:\...\backend_django\empresas\models.py

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

# --- I. Modelo Empresa (Tenant) ---
class Empresa(models.Model):
    """Modelo central que representa al cliente (Studio) de AXIOM."""
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Nombre de la Empresa/Studio")
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Empresa (Tenant)"
        verbose_name_plural = "Empresas (Tenants)"

    def __str__(self):
        return self.nombre

# --- II. Modelo Paquete ---
class Paquete(models.Model):
    """Define los productos de clases en bloque para la venta."""
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE, 
        related_name='paquetes', # related_name más limpio
        verbose_name="Disponible para Empresa"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_creditos = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Número de Créditos Incluidos"
    )
    
    class Meta:
        verbose_name = "Paquete de Créditos"
        verbose_name_plural = "Paquetes de Créditos"

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_creditos} créditos)"

# --- III. Modelo Crédito de Alumno ---
class CreditoAlumno(models.Model):
    """Gestiona el saldo de créditos restantes de un alumno tras la compra."""
    alumno = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Usa settings.AUTH_USER_MODEL para referenciar al modelo Usuario
        on_delete=models.CASCADE, 
        related_name='creditos_otorgados_empresa', 
        verbose_name="Alumno Propietario"
    )
    paquete = models.ForeignKey(
        Paquete, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True,
        verbose_name="Paquete Adquirido"
    )
    # Referencia de cadena CRÍTICA para evitar dependencia circular
    sede = models.ForeignKey(
        "sedes.Sede", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Sede donde se compró"
        # related_name no es estrictamente necesario aquí si no se consulta desde Sede
    )
    creditos_restantes = models.IntegerField(default=0, verbose_name="Créditos Restantes")
    fecha_compra = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Crédito de Alumno"
        verbose_name_plural = "Créditos de Alumnos"

    def __str__(self):
        return f"Créditos de {self.alumno.email} - {self.creditos_restantes} restantes"