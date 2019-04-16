FROM python:3.6-alpine3.9

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt


COPY . /app
WORKDIR /app

#Setup API User
RUN addgroup api && adduser -DH -G api apiuser
RUN chown apiuser:api -R /app


CMD ["/app/startCeleryWorker"]