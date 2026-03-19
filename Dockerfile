FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY backend_django/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend_django/ ./backend_django/

WORKDIR /app/backend_django

RUN python manage.py collectstatic --noinput || true

ENV PORT=8000
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --fake-initial && python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"]
