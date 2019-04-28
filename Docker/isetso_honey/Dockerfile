#
#

FROM debian:stretch-slim

# install selected

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	python \
	python-pip \
	python-mysqldb \
	&& rm -rf /var/lib/apt/lists/*
	
# install git & clone project from github

RUN apt-get update \
        && apt-get install -y --no-install-recommends git \
	&& git clone https://github.com/anouarbensaad/IoT-Honeypot \
	&& rm -rf /var/lib/apt/lists/* \
        && apt-get clean \
        && rm -rf /tmp/* /var/tmp/* /usr/share/doc/*

#install mysql-connector package

RUN pip install mysql-connector-python


WORKDIR IoT-Honeypot
ENTRYPOINT [ "python" , "honeyserver.py" ]

EXPOSE 999
