#!/bin/sh
set -e

until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

export DATABASE_URL=postgis://$POSTGRES_USER:$POSTGRES_PASSWORD@db:5432/$POSTGRES_USER

exec "$@"
