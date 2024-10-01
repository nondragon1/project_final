FROM python:3.9

COPY ./ /app

RUN apt-get update && apt-get install -y gcc && pip install --upgrade -r /app/requirements.txt

EXPOSE 8000

CMD [ "python" , "/app/manage.py" , "runserver"  , "0.0.0.0:8000"]
