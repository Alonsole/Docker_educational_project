## Добро пожаловать на ветку Задачи №1 
[Ссылка на задание](https://github.com/netology-code/py-homeworks-web/tree/new/1.3-docker "Домашнее задание к лекции «Docker»")  

Создан docker image с Http сервером Nginx.  
Заменена страница приветсвия Nginx на свою (изменён текст приветствия).  
```Docker
#Использован официальный, одобренный релиз 1.27 nginx
FROM nginx:1.27
LABEL authors="Maksim Velichko"
# Копирую index.html в каталог nginx
COPY /html/index.html /usr/share/nginx/html/
```  
### Сборка Docker-образа  
Выполните команду в терминале из каталога, где находится Dockerfile.  
```Docker
docker image build . --tag=my-nginx_v:0.01
```
### Запуск контейнера  
Выполните команду в терминале из каталога, где находится Dockerfile.  
```Docker
docker run -d -p 8080:80 my-nginx_v:0.01
```
### Проверяем результат
Откройте браузер и перейдите по адресу:
```Docker
 http://localhost:8080. 
```
Вы должны увидеть вашу изменённую страницу приветствия.
Готово! Теперь у вас запущен Docker-образ с настроенным веб-сервером Nginx с
кастомной страницей приветствия.