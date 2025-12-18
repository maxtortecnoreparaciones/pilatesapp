PR: Fix segregacion/clases endpoint and tests

Resumen
- Se arregló el bloqueo 404 y se validó la segregación por Estudio/Sede.
- Se añadieron y/o ajustaron modelos, views, serializers, urls y tests para cumplir RF1.1.

Archivos modificados (resumen):
- clases/urls.py: reordenado para exponer la ruta custom `clases/disponibles/` antes del router.
- clases/views.py: `ClaseListView.get_queryset()` filtra por `request.user.estudio` y `request.user.sede`.
- clases/serializers.py: Serializer para Clase.
- clases/tests_segregacion.py: tests de segregación (APITestCase).
- estudios/models.py, sedes/models.py, usuarios/models.py: modelos ajustados para evitar defaults inválidos y cumplir RF1.1.
- config/test_settings.py: settings de test (SQLite en memoria) para ejecutar tests en CI/local.
- config/settings.py: añadido 'estudios' a INSTALLED_APPS.

Salida de tests (Docker):
- Comando ejecutado:
  docker-compose run --rm backend sh -c "python manage.py test --settings=config.test_settings"

- Resultado final:
  Found 2 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ..
  Ran 2 tests in 0.094s
  OK

Instrucciones para crear la rama y el PR (PowerShell):

# Crear rama local y commitear
git checkout -b fix/clases-segregacion-tests
git add clases/urls.py clases/views.py clases/serializers.py clases/tests_segregacion.py config/test_settings.py config/settings.py estudios/models.py sedes/models.py usuarios/models.py
git commit -m "Fix: expose clases/disponibles route before router; enforce RF1.1 filtering; add tests and test settings"

a) Si usas GitHub CLI (gh) para crear PR:
git push -u origin fix/clases-segregacion-tests
gh pr create --fill --base main --head fix/clases-segregacion-tests

b) Si no usas gh, empuja la rama y abre PR desde la interfaz web:
git push -u origin fix/clases-segregacion-tests
# Luego abre https://github.com/<tu-org>/<tu-repo>/compare y crea el PR manualmente.

Notas adicionales
- Se limpiaron contenedores huérfanos con: docker-compose down --remove-orphans
- Si quieres, puedo intentar crear el PR automáticamente si me autorizas a ejecutar git push en este entorno (necesitaría credenciales/configuración remota)."}]}'}]}]}'
