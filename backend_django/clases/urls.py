from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClaseViewSet, AgendamientoViewSet, ClaseListView

router = DefaultRouter()
router.register(r'clases', ClaseViewSet)
router.register(r'agendamientos', AgendamientoViewSet)

urlpatterns = [
    path('clases/disponibles/', ClaseListView.as_view(), name='clases-disponibles'),
    path('', include(router.urls)),
]