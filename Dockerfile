FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV LISTEN_PORT 8090

COPY ./app /app

RUN chmod -R 755 /app

WORKDIR /app