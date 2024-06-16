FROM python:3.12-slim-bookworm

LABEL maintainer="Akshay Dadwdal <akshayd00@outlook.com>"

RUN apt-get update && apt-get install -y vim git

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir pipenv==2024.0.1

RUN pipenv install --system --deploy

ENTRYPOINT [ "./start.sh" ]
