FROM python:3.11-slim

WORKDIR /app
COPY app.py /app

RUN apt-get update && apt-get install -y \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*  # Bersihkan cache agar ukuran image lebih kecil

RUN pip install flask flask_httpauth

EXPOSE 638
CMD ["python", "app.py"]

