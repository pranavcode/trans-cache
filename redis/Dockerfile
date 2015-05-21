# Redis server non-persistent cache-only image
FROM centos:centos7

MAINTAINER Pranav Kulkarni <pranavcode@gmail.com>

LABEL Description="Redis Server Non Persistent Cache Only image" \
      VERSION=0.01

RUN yum --noplugins -y update

RUN rm -f /var/lib/rpm/__* && \
    rpm --rebuilddb -v -v && \
    rm -f /var/cache/timedhosts.txt

RUN yum -y install deltarpm && \
    yum -y install epel-release && \
    yum -y install git wget which curl tar bash unzip hostname logrotate
    
ENV REDIS_DOWNLOAD_URL="http://download.redis.io/releases/redis-3.0.1.tar.gz" \
    REDIS_DOWNLOAD_SHA1="fe1d06599042bfe6a0e738542f302ce9533dde88"

RUN buildDeps='gcc libc6-dev make'; \
    yum update && \
    yum -y install $buildDeps && \
    mkdir -p /usr/src/redis && \
    curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.tar.gz && \
    echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - && \
    tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 && \
    rm -f redis.tar.gz && \
    make -C /usr/src/redis && \
    make -C /usr/src/redis install && \
    rm -rf /usr/src/redis && \
    yum -y remove $buildDeps && \
    yum -y autoremove

ADD redis.conf /etc/redis.conf

EXPOSE 6379
CMD [ "redis-server", "/etc/redis.conf" ]
