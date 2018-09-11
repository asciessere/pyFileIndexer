#
#	DOCKERFILE: pyFileIndexer-app
#
# Using pyFileIndexer-env as a starting point, copies all the application files.
#

FROM pyfileindexer-env:latest

ENV APP_HOME /home/pyFileIndexer/
WORKDIR $APP_HOME

COPY db.py .
COPY duplicates.py .
COPY hashing.py .
COPY pyFileIndexer.py .

