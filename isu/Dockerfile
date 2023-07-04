FROM python:latest

WORKDIR /isu

COPY ./requirements.txt /isu/requirements.txt

RUN pip install psycopg2

RUN pip install -r /isu/requirements.txt

COPY . .

EXPOSE 8000

