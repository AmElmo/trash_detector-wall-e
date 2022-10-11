
# Stage 0

FROM node:12.16.3-alpine as build

WORKDIR /app
COPY package*.json ./

RUN npm install
COPY . .
RUN npm run build

# Stage 1

FROM fholzer/nginx-brotli:v1.12.2

WORKDIR /etc/nginx
ADD nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]
