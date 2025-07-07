# Gunakan base image node
FROM node:18-alpine

# Buat folder kerja di container
WORKDIR /app

# Salin file package.json dan install dependency
COPY package*.json ./
RUN npm install

# Salin semua source code ke dalam container
COPY . .

# Expose port yang digunakan Express
EXPOSE 3000

# Jalankan server saat container start
CMD ["node", "server.js"]

