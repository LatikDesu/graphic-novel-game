#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

alembic revision --autogenerate -m "Migration"
alembic upgrade head
export PGPASSWORD=postgres
pg_restore -h db -U postgres -W -d game_db database.sql


exec "$@"