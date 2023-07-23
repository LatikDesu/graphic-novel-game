FROM python:3

WORKDIR /code/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /code/backend/requirements.txt
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --no-cache-dir --upgrade -r /code/backend/requirements.txt

COPY . /code/backend

EXPOSE 8000

