FROM thanawat1303/workout-app:0.0.2
# FROM python:3.9
# FROM python:3.9-slim

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libffi-dev \
    libpq-dev \
    python3-dev \
    build-essential
# RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /app/requirements.txt --timeout=120

# EXPOSE 8000

# CMD [ "python" , "/app/manage.py" , "runserver"  , "0.0.0.0:8000"]
