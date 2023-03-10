FROM python:3.11.2-alpine3.17

WORKDIR /test

RUN apk update \
    && pip install --upgrade pip \
    && pip install pymysql \
    && pip install mysql-client \
    && pip install requests

WORKDIR /test
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
