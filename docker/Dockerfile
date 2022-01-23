FROM python:3.8

RUN mkdir -p /app/code

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/code

CMD python manage.py runserver
