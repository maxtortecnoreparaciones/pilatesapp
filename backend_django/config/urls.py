from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URL de registro de usuario
    path('api/', include('usuarios.urls')),

    # URLs de la API para tus otras aplicaciones
    path('api/', include('sedes.urls')),
    path('api/', include('clases.urls')),
    
    # URLs de autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]