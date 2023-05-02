FROM node:18-alpine as builder
WORKDIR /usr/app
COPY ./app ./

FROM nginx
EXPOSE 3000

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /usr/app /usr/share/nginx/html
