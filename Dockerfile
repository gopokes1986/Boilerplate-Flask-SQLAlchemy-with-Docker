FROM ubuntu:latest
MAINTAINER Your Name "your@email"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3.7 build-essential gcc git libmysqlclient-dev

COPY . /flask_sqlalchemy_backbone_with_docker
WORKDIR /flask_sqlalchemy_backbone_with_docker

RUN pip3 install --upgrade setuptools && pip3 install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app/run.py

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "run:app"]
