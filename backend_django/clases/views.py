from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Clase, Agendamiento
from .serializers import ClaseSerializer, AgendamientoSerializer

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class AgendamientoViewSet(viewsets.ModelViewSet):
    queryset = Agendamiento.objects.all()
    serializer_class = AgendamientoSerializer

class ClaseListView(generics.ListAPIView):
    serializer_class = ClaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # RF1.1: Solo clases del mismo estudio y sede que el usuario
        return Clase.objects.filter(sede__estudio=user.estudio, sede=user.sede)