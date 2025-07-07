# Gunakan base image yang kecil
FROM python:3.12-alpine

# Set workdir
WORKDIR /app

# Install git buat clone repo
RUN apk add --no-cache git

# Clone project dari GitHub
RUN git clone https://github.com/bgstaal/multipleWindow3dScene.git .

# Expose port 80
EXPOSE 89

# Jalankan simple HTTP server
CMD ["python3", "-m", "http.server", "89"]

