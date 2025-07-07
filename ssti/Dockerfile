FROM python:3.11-slim

WORKDIR /app

# Install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

