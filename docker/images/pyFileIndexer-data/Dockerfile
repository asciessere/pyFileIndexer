
#
#	DOCKERFILE: pyFileIndexer-data
#
# Docker container used as VOLUME, contains only the files that will
# be read by pyFileIndexer-app jobs.
#

FROM debian:stretch-slim

WORKDIR /home/pyFileIndexer/data

#
#	CHANGE HERE to copy the data you want to be analysed.
#
COPY epubs .

