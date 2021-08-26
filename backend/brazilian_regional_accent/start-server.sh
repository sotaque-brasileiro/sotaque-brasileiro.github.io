#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
  (cd /app; python manage.py createsuperuser --no-input)
fi
(cd /app; gunicorn brazilian_regional_accent.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3) &
nginx -g "daemon off;"
