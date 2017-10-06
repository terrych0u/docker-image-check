FROM python:2.7.14-alpine
MAINTAINER terry chou <tequilas721@gmail.com>

COPY requirements.txt /tmp/requirements.txt
COPY CheckDockerUpdate.py /usr/local/bin/CheckDockerUpdate.py

RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["/usr/local/bin/CheckDockerUpdate.py"]

