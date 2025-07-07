# Menggunakan image Python sebagai base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt /app/requirements.txt

# Instalasi dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file ke dalam container
COPY . /app

# Menentukan port yang akan digunakan oleh aplikasi
EXPOSE 6723

# Menjalankan aplikasi Flask saat container dijalankan
CMD ["python", "app.py"]

