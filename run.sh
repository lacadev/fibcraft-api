#! /bin/bash

flask init-db
gunicorn --bind 0.0.0.0:8000 "$FLASK_APP:create_app()"
