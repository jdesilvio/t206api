# T206 REST API


### Getting started

1. Build environment

    `docker-compose build`

1. Start containers

    `docker-compose up`

1. Go into app container

    `docker exec -it t206api_web_1 bash`

1. Import data

    `python manage.py load_data`


### Management scripts

    python manage.py --help


### Database Migrations

__Uses `Flask-Migrate`__

```bash
# Initialize database
env/bin/flask bd init

# Create migration
env/bin/flask db migrate

# Apply migration
env/bin/flask db upgrade
```
