FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN apt-get update
RUN apt-get install -y build-essential libevent-dev python-dev


ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install pip-tools
RUN pip install gunicorn
RUN pip install supervisor
ADD . /code/

# Define mountable directories.
VOLUME ["/etc/supervisor/conf.d"]

# Define working directory.
WORKDIR /etc/supervisor/conf.d

ADD conf/supervisor/supervisord.conf /etc/supervisor/
# Define default command.
CMD ["supervisord", "-c", "/code/conf/supervisor/supervisord.conf"]
#CMD ["python", "-u", "/code/flask/api/api.py"]