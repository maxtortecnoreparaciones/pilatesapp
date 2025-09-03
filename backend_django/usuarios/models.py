
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es un campo obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', 'Administrador')
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('Profesor', 'Profesor'),
        ('Alumno', 'Alumno'),
        ('Administrador', 'Administrador'),
    ]
    NIVELES_ALUMNO = [
        ('Básico', 'Básico'),
        ('Estándar', 'Estándar'),
        ('Premium', 'Premium'),
    ]
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES)
    nivel_alumno = models.CharField(max_length=20, choices=NIVELES_ALUMNO, null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    insignias_cliente = models.JSONField(default=list, blank=True)
    calificacion_profesor = models.FloatField(null=True, blank=True)
    plantilla_huella = models.BinaryField(null=True, blank=True)
    numero_telefono = PhoneNumberField(null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'rol']

    def __str__(self):
        return self.email