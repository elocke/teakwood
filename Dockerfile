FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get install -y \
	build-essential \
	libevent-dev \
	python-dev



ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/