# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY livetrack.py ./
COPY index.html ./

RUN pip install flask folium opencage phonenumbers

EXPOSE 5050

CMD ["python", "livetrack.py"]

