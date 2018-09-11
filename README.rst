
pyFileIndexer
=============

A simple file indexer using Python, Redis and Docker.

Given some search paths, every file will be indexed based on its hash (MD5, SHA-1 or SHA-256 for now) and stored on a Redis list; making it possible to search for duplicates, add metadata, etc.

This is a personal project with the intent of learning Python, Redis and Docker.


How It Works
------------

There are separate containers for Redis and for each Python *job* that will analyse files and add data; there's also a separate container with the files that will be analysed. Each one is brought up with a separate docker-compose file.

There's only one Python application, which will perform a different job based on the *environment variables* specified in each container.

Once the Redis server is up and running, the first job to be executed performs the **hashing**. It'll save a list of every hash found for every file, along with a counter (Redis' Sorted Set **score**) and a second Set will associate every file path to its hashes, if there's more than one.

Very subsequent job will work with this data, so it could, for example, find duplicate files (same hash) or add metadata for a subset of files.


Example
-------

Building the Images
~~~~~~~~~~~~~~~~~~~

We'll start with the environment image containing Python and the Redis python module.

``docker build -t pyfileindexer-env docker/images/pyFileIndexer-env/``

Then the image containg all the files you want to index.

One thing to consider here is that the Dockerfile will copy each specified dir (or file) to a container that will be used as a *volume* by the other containers; and this volume won't change until you build the image again with different files.

Also, these files must be acessible by the docker machine when building the image. Right now the Dockerfile is copying a dir called ``epubs`` from the same location of the Dockerfile, in ``docker/image/pyFileIndexer-data`` to the image, but anything in the volume will be analysed. Just remember to change the Dockerfile according to your preferences.

Once this is done, we build it:

``docker build -t pyfileindexer-data docker/images/pyFileIndexer-data/``

For the application image, just make sure all the ``.py`` files are in the same directory as the Dockerfile.

``docker build -t pyfileindexer-app docker/images/pyFileIndexer-app/``

Running the Containers
~~~~~~~~~~~~~~~~~~~~~~

We want to keep our containers organized, so we will use a project name when interacting with docker-compose. Let's just use ``pfi`` for now.

First we bring up the Redis server as a detached container:

(on ``docker\redis-server``)

``docker-compose -p pfi up -d``

The hashing job will bring up both the application and the data containers, and save all information on Redis.

(on ``docker\job-hashing``)

``docker-compose -p pfi up``

The duplicates job will search for duplicate hashes and print the file locations to the console.

(on ``docker\job-duplicates``)

``docker-compose -p pfi up``

To bring all the containers down, always on the specific directory:
``docker-compose -p pfi down``

