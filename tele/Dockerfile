# Gunakan image Node.js
FROM node:18

# Set workdir
WORKDIR /app

# Copy file konfigurasi
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy semua file ke dalam container
COPY . .

# Jalankan aplikasi
CMD ["npm", "start"]

