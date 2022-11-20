FROM node:alpine

COPY . /opt/front
WORKDIR /opt/front

ENV NODE_ENV production
ENV API_URL https://api.frhack.marcpartensky.com
RUN npm i
RUN npm run build
RUN npm i -g serve

ENTRYPOINT [ "serve", "-s", "build"]
