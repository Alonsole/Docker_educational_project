# Использую образ Nginx как базовый
FROM nginx:1.27
LABEL authors="Maksim Velichko"
# Копирую index.html в каталог nginx
COPY /html/index.html /usr/share/nginx/html/