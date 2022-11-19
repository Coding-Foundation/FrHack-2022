FROM node:alpine

COPY . /opt/front
WORKDIR /opt/front

RUN npm i

ENTRYPOINT [ "npm", "start" ]
