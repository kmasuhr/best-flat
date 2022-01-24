FROM python:3.9-alpine

ENV DJANGO_SETTINGS_MODULE=flats_ui.settings
ENV PORT=8000

RUN mkdir -p /app/code && \
    apk update && apk add python3-dev gcc libc-dev libffi-dev openssl-dev

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/code

ADD . .

CMD ./start.sh
