#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
  (cd /app; python manage.py createsuperuser --no-input)
fi
(cd /app; gunicorn brazilian_regional_accent.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 8 --timeout 0 --user www-data) &
nginx -g "daemon off;"
