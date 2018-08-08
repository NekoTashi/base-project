FROM mdillon/postgis:9.6-alpine

# -- Adding create extensions script
COPY ./compose/prod/db/add_extensions.sh /docker-entrypoint-initdb.d/
