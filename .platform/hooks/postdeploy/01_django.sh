#!/bin/bash

source /var/app/venv/*/bin/activate && {

# collecting static files
python manage.py collectstatic --noinput;
# log which migrations have already been applied
python manage.py showmigrations;
# migrate the rest
python manage.py migrate --noinput;
# import seeds
python manage.py loaddata ./info_service/fixtures/coreapp_seeds.json
}