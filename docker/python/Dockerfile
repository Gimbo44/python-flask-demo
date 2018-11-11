FROM python:3.6.7-stretch

RUN apt-get update \
    && apt-get install -y \
        python3-pip \
        python3-dev \
        build-essential

COPY . /app
WORKDIR /app

RUN  pip3 install -r requirements.txt

EXPOSE 5000