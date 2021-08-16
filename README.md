# car_info_retriever
## Quick Start for development local environment

First, run a Postgresql database with Docker:

1. Run `docker compose up`

Use Virtual env is for format checking in VSCode

1. go to your project folder
2. install virtual env: `pip install virtualenv`
3. create a virtual env: `virtualenv .venv`
4. activate virtual env: `source .venv/bin/activate`, check if your python path is correct
5. install packages: `pip install -r requirements.txt`

Start the Django server

1. Migrate database `python manage.py migrate`
2. Run Django Server `python manage.py runserver 9400`


## Testing

1. Run all tests `./manage.py test -v 2`
