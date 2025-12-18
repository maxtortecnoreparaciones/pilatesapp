from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SedeViewSet

router = DefaultRouter()
router.register(r'sedes', SedeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]