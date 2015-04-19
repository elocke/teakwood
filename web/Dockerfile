FROM python:2.7.9-onbuild

ENV PYTHONUNBUFFERED 1
# RUN apt-get update
# RUN apt-get install -y software-properties-common python-software-properties
RUN apt-get update
RUN apt-get install -y build-essential libevent-dev python-dev

#COPY . /usr/src/app/
WORKDIR /usr/src/app/web