# Gunakan image python terbaru
FROM python:3.10-slim

# Set direktori kerja
WORKDIR /app

# Salin semua file
COPY . .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask
EXPOSE 2628

# Jalankan aplikasi
CMD ["python", "app.py"]

