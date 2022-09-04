#!/bin/bash

echo "Make migrations"
python3 manage.py makemigrations

echo "Apply database migrations"
python3 manage.py migrate

exec "$@"
