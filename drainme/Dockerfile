FROM node:18-alpine

WORKDIR /app

RUN npm install -g hardhat

COPY . ./
RUN npm install

CMD ["npx", "hardhat", "node"]
