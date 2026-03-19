FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Instalar dependencias del sistema para psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero para aprovechar caché
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY . .

# Recolección de archivos estáticos
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Railway usa PORT o PORT environment variable
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"]
