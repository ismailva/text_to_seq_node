FROM python:3.12.7-slim

WORKDIR /app

RUN apt-get update -y

COPY requirments.txt /app/
RUN pip install --no-cache-dir -r requirments.txt

COPY src /app/src/
COPY data /app/data/
COPY test /app/test/
COPY fastapi_main.py /app/
COPY main.py /app/
COPY entrypoint.sh /app/

EXPOSE 8501
EXPOSE 8080

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]