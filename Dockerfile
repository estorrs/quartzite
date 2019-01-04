FROM python:3.6-jessie

RUN apt-get update && apt-get install -y vim

RUN pip install pytest

COPY . /quartzite
WORKDIR /quartzite

CMD /bin/bash
