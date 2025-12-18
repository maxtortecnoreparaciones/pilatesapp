from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator


# =============================
#   CUSTOM USER MANAGER
# =============================
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Crea un usuario normal."""
        if not email:
            raise ValueError("El email es obligatorio")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Crea un superusuario."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('rol', 'Administrador Global')
        # Se elimina la línea que asigna estudio=None para evitar el error TypeError
        return self.create_user(email, password, **extra_fields)


# =============================
#       MODELO USUARIO
# =============================
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre_completo = models.CharField(max_length=255)

    # ------------------------------------------
    #   FIX REAL DEL ERROR TypeError (ciclos)
    # ------------------------------------------
    # Mientras NO existan migraciones iniciales,
    # estos campos deben permitir NULL.
    # Luego podemos hacerlos obligatorios.
    estudio = models.ForeignKey(
        "estudios.Estudio",
        on_delete=models.CASCADE,
        related_name="usuarios",
        help_text="Empresa/Tenant al que pertenece este usuario."
    )

    sede = models.ForeignKey(
        "sedes.Sede",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="usuarios_sede"
    )

    # -------------------
    #   CAMPOS DEL SISTEMA
    # -------------------
    rol = models.CharField(max_length=100, default="Alumno")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre_completo", "rol"]

    def __str__(self):
        return self.email
