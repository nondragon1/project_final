# create file .env and setup val
# EMAIL_PASS=<app-key-email>

docker-compose --env-file .env -f docker-compose.yml up -d

# add superuser
python /app/manage.py createsuperuser