FROM python:3.7.5-slim-buster

## install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

## set environment variables TODO: why?
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

## TODO: user or no user?
## add user
# RUN addgroup --system user && adduser --system --no-create-home --group user
# RUN chown -R user:user /usr/src/app && chmod -R 755 /usr/src/app

## add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

## switch to non-root user
# USER user

COPY . /usr/src/app

ENV FLASK_ENV development
ENV FLASK_APP flask_app.py
CMD ["python3", "-m", "flask", "run", "--port", "3000", "--host", "0.0.0.0"]
