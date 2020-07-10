FROM python:3.6-slim-buster

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
  && rm requirements.txt

COPY . /app
WORKDIR /app

#Setup API User
RUN useradd -r -U -m apiuser \
  && chown apiuser:apiuser -R /app

USER apiuser

EXPOSE 8080
CMD ["gunicorn", "--config=gunicorn.py", "api.wsgi:application"]
