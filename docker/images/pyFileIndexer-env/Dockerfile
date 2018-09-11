#
#	DOCKERFILE: pyFileIndexer-env
#
# Separate dockerfile for the application requirements, since they
# don't change as much and take longer to build.
#

FROM debian:stretch-slim

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	python3 \
	python3-pip \
&& rm -rf /var/lib/apt/lists/* \
&& pip3 install redis

