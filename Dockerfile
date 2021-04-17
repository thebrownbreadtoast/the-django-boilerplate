FROM python:alpine3.13

MAINTAINER "Akshay Dadwdal <akshayd00@outlook.com>"

RUN apk update && apk add --no-cache vim \
                                     git

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install --no-cache pipenv==2020.11.15

ENTRYPOINT "./start.sh"