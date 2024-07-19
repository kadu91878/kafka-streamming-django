#!/bin/bash

# Aplique as migrações do Django
python manage.py makemigrations
python manage.py migrate

# Execute o comando recebido como argumento
exec "$@"
