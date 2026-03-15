FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY src src
RUN pip install --no-cache-dir -r src/requirements.txt

CMD ["/bin/sh"]
#podman run --name vector01 -d -it es_vectorizer /bin/sh