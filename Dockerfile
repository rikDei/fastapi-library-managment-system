FROM python:3.12.11-alpine3.22

WORKDIR /

COPY /app /app
COPY /database /database

RUN apt-get update && apt-get install -y curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

CMD ["python", "-m", "fastapi", "dev", "app"]
