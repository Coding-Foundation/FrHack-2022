FROM python:3.9.4-alpine

COPY . /app
WORKDIR /app

RUN apk update && apk upgrade && apk fix && apk del
RUN apk add curl
RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "-f", "localhost:80" ]

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
