FROM python:2.7.14-alpine
MAINTAINER terry chou <tequilas721@gmail.com>

ADD requirements.txt /tmp/requirements.txt
ADD CheckDockerUpdate.py /usr/local/bin/CheckDockerUpdate.py

RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["/usr/local/bin/CheckDockerUpdate.py"]

