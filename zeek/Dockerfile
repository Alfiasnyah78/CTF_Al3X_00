# Base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    # tools if needed, for snort/suricata logs, add here if needed \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

WORKDIR /app/backend

RUN pip install -r requirements.txt

# Serve frontend + backend together with simple python HTTP server for frontend
# We'll use flask for API and serve frontend as static files through flask

# Move frontend into backend folder to serve via flask
RUN mv ../frontend ./frontend

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=78"]

