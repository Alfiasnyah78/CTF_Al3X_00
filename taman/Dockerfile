# Gunakan image Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin semua file ke dalam kontainer
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port untuk aplikasi
EXPOSE 6000

# Jalankan aplikasi
CMD ["python", "app.py"]

