from django.urls import path
from .views import RegistroView

urlpatterns = [
    path('auth/registro/', RegistroView.as_view(), name='auth_registro'),
]