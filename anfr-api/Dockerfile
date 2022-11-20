FROM python:alpine

COPY . /opt/anfr/api
WORKDIR /opt/anfr/api

RUN pip install -Ur requirements.txt

EXPOSE 80

# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "-f", "localhost:80" ]

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
