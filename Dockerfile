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