from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.apps import apps

class SegregacionMultiSedeTestCase(APITestCase):
    def setUp(self):
        Estudio = apps.get_model('estudios', 'Estudio')
        Sede = apps.get_model('sedes', 'Sede')
        Usuario = apps.get_model('usuarios', 'Usuario')
        Clase = apps.get_model('clases', 'Clase')

        # Crear estudios
        self.estudio_a = Estudio.objects.create(nombre="Estudio A", slug="estudio-a")
        self.estudio_b = Estudio.objects.create(nombre="Estudio B", slug="estudio-b")

        # Crear sedes
        self.sede_a1 = Sede.objects.create(estudio=self.estudio_a, nombre="Sede A1", direccion="Dir A1")
        self.sede_b1 = Sede.objects.create(estudio=self.estudio_b, nombre="Sede B1", direccion="Dir B1")

        # Crear usuarios
        self.alumno_a = Usuario.objects.create_user(
            email="alumnoa@example.com",
            password="testpass123",
            nombre_completo="Alumno A",
            estudio=self.estudio_a,
            sede=self.sede_a1,
            rol="Alumno"
        )
        self.alumno_b = Usuario.objects.create_user(
            email="alumnob@example.com",
            password="testpass123",
            nombre_completo="Alumno B",
            estudio=self.estudio_b,
            sede=self.sede_b1,
            rol="Alumno"
        )

        # Crear clases en cada sede
        for i in range(5):
            Clase.objects.create(
                sede=self.sede_a1,
                profesor=self.alumno_a,  # Para test, el alumno es profesor
                tipo_disciplina=f"Disciplina A{i+1}",
                fecha_hora=f"2025-12-0{i+1}T10:00:00Z",
                cupos_totales=10,
                cupos_disponibles=10
            )
            Clase.objects.create(
                sede=self.sede_b1,
                profesor=self.alumno_b,
                tipo_disciplina=f"Disciplina B{i+1}",
                fecha_hora=f"2025-12-0{i+1}T11:00:00Z",
                cupos_totales=10,
                cupos_disponibles=10
            )

        # Token para autenticación
        self.token_a = Token.objects.create(user=self.alumno_a)

    def test_alumno_solo_ve_clases_de_su_sede_y_tenant(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token_a.key}')
        url = '/api/clases/disponibles/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        clases = response.data if isinstance(response.data, list) else response.data.get('results', [])
        self.assertEqual(len(clases), 5)
        for clase in clases:
            self.assertEqual(clase['sede'], self.sede_a1.id)
            self.assertNotIn('B', clase['tipo_disciplina'])

    def test_acceso_denegado_sin_autenticar(self):
        url = '/api/clases/disponibles/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
