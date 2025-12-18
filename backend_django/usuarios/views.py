from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Usuario
from .serializers import UsuarioSerializer

class RegistroView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny] # Permitir acceso sin autenticación para el registro    