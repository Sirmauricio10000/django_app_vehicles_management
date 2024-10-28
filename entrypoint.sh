#!/bin/sh

# Ejecutar migraciones
python manage.py migrate --no-input

# Crear superusuario si no existe
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \
    User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"

# Ejecutar el servidor
exec "$@"
