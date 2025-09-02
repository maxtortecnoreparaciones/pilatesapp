from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Clase, Usuario, Agendamiento
from .serializers import ClaseSerializer, UsuarioSerializer, AgendamientoSerializer

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = [IsAuthenticated]

class AgendamientoViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Agendamiento.objects.all()
    serializer_class = AgendamientoSerializer
    permission_classes = [IsAuthenticated]