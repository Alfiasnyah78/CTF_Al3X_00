FROM python:3.11-slim

# Install socat
RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY encrypt_challenge.py .

EXPOSE 5430

CMD ["socat", "TCP-LISTEN:5430,reuseaddr,fork", "EXEC:python3 /app/encrypt_challenge.py"]

