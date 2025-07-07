# Stage 1: build
FROM node:18-alpine AS builder
WORKDIR /app
COPY . .
RUN npm install

# Stage 1: build frontend
FROM node:18-alpine AS builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Stage 2: serve with nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8567
CMD ["nginx", "-g", "daemon off;"]

