docker-compose run backend python backend/manage.py collectstatic
docker-compose run backend python backend/manage.py makemigrations
docker-compose run backend python backend/manage.py migrate