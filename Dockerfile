FROM python:3.11-alpine3.19

LABEL maintainer="Akshay Dadwdal <akshayd00@outlook.com>"

RUN apk update && apk add --no-cache vim

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install --no-cache pipenv==2023.11.15

RUN pipenv install --system --deploy

ENTRYPOINT "./start.sh"