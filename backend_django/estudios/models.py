from django.db import models
from django.utils.text import slugify


class Estudio(models.Model):
    """
    Modelo que representa un Tenant (Estudio / Empresa cliente) en la arquitectura
    multi-tenant. Es intencionalmente simple: otros modelos lo referencian mediante
    FK.

    Campos:
    - nombre: nombre público y único del estudio.
    - slug: identificador legible en URLs, único.
    - fecha_creacion: timestamp de creación.
    """

    nombre = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    logo_url = models.URLField(max_length=300, blank=True, null=True, help_text="URL del logo para personalización de marca")
    contacto_email = models.EmailField(blank=True, null=True, help_text="Email de contacto administrativo")

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        # Genera un slug a partir del nombre si no se proporcionó uno.
        if not self.slug and self.nombre:
            base = slugify(self.nombre)[:140]
            slug_candidate = base
            counter = 1
            # Asegurar unicidad del slug
            ModelClass = self.__class__
            while ModelClass.objects.filter(slug=slug_candidate).exclude(pk=self.pk).exists():
                slug_candidate = f"{base}-{counter}"
                counter += 1
            self.slug = slug_candidate
        super().save(*args, **kwargs)
