FROM node:alpine

# ENV NODE_ENV production
ENV API_URL https://api.frhack.marcpartensky.com

COPY . /opt/front
WORKDIR /opt/front

RUN npm i
RUN npm run build
RUN npm i -g serve

ENTRYPOINT [ "serve", "-s", "build"]
