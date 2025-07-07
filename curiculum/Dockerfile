FROM nginx:alpine

# Buat folder konten web
WORKDIR /usr/share/nginx/html

# Hapus default Nginx index
RUN rm -rf ./*

# Salin index.html dan assets
COPY index.html .
COPY assets ./assets

# Salin konfigurasi custom Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 1973

CMD ["nginx", "-g", "daemon off;"]

