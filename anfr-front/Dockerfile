FROM node:alpine

COPY . /opt/front
WORKDIR /opt/front

RUN npm i
RUN npm run build
RUN npm i -g serve

ENTRYPOINT [ "serve", "-s", "build"]
