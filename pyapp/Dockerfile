# Python client to write http_requests and http_responses to redis cache
FROM ubuntu:14.04

MAINTAINER Pranav Kulkarni <pranavcode@gmail.com>

LABEL Description="Python image to read/write http_requests/http_responses to/from redis cache." \
      VERSION=0.01

RUN apt-get -y update && \ 
    apt-get -y install python python-pip

# Install redis client
RUN pip install redis requests

# Mount volumes
VOLUME /data
VOLUME /app

# Push all scripts into home
ADD scripts/* /app/

# Test file
ADD data/* /data/

RUN chmod a+x /app/*
