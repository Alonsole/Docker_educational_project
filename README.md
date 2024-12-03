## Добро пожаловать на ветку Задачи №2
[Ссылка на задание](https://github.com/netology-code/py-homeworks-web/tree/new/1.3-docker "Домашнее задание к лекции «Docker»")  

Создание контейнера для REST API сервера по проекту из курса по Django - [Django_crud](https://github.com/Alonsole/Django_crud)   
Заменена БД с postgresql на sqlite3.   
Вынесены зависимости в .env  
Параметры передаюся на стадии запуска  
```
Django config
PROJECT_HOST=
Django_Secret=
DEBUG=
```

Настройка Dockerfile 
```Docker
FROM python:3.10
WORKDIR /app
ENV PYTHONDONTRITEBYTECODE="1"
ENV PYTHONBUFFERED="1"
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV MY_ENV=test_03_12
EXPOSE 5050
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD ["python3", "-u", "manage.py", "runserver", "0.0.0.0:5050"]
```  
### Сборка Docker-образа  
Выполните команду в терминале из каталога, где находится Dockerfile.  
```Docker
docker image build . --tag=test_03_12:v0.0.4
```
### Запуск контейнера  
Выполните команду в терминале из каталога, где находится Dockerfile.  
```Docker
docker run -d -e DJANGO_SECRET="Ваш секретный ключ" -e DEBUG=True -e PROJECT_HOST=localhost -p 5050:5050 test_03_12:v0.0.4
```
### Проверяем результат
Откройте браузер и перейдите по адресу:
```Docker
 http://localhost:5050/api/v1/ 
```
Вы должны увидеть Api интерфейс.  

Тесты/Запросы в файле requests-examples.http