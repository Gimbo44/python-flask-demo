FROM python:3.6.7-stretch

RUN apt-get update \
    && apt-get install -y \
        python3-pip \
        python3-dev \
        build-essential \
    && virtualenv venv \
    && source venv/bin/activate \
    && pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000