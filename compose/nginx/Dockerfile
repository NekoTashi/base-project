FROM nginx:1.15.2-alpine

# -- Adding nginx.conf and default.conf inside the container
COPY ./compose/prod/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./compose/prod/nginx/default.conf /etc/nginx/conf.d/default.conf
