FROM alpine:3.16

LABEL maintaner="Vadym Bezdytnyi"
LABEL description="This is an image with simple echo server written on Python"
LABEL version="1.0"

ENV PORT=3000
ENV HOST="0.0.0.0"

RUN apk update && apk add --no-cache python3 py3-pip curl
WORKDIR /app
COPY . .

EXPOSE 3000

ENTRYPOINT ["python3", "echo-server.py"]