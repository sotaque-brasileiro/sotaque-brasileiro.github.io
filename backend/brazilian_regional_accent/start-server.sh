#!/usr/bin/env bash
# start-server.sh
(cd /app; gunicorn brazilian_regional_accent.wsgi --bind 0.0.0.0:80 --workers 1 --threads 8 --timeout 0 --user www-data)
