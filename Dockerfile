FROM python:3.9-slim-buster

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN apk update && apk upgrade
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app_main.py"]