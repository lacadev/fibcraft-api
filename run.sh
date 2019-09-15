#! /bin/bash

flask init-db
gunicorn --bind 0.0.0.0:8000 "fibcraft:create_app()"
