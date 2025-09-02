from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaseViewSet, UsuarioViewSet, AgendamientoViewSet

router = DefaultRouter()
router.register(r'clases', ClaseViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'agendamientos', AgendamientoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]