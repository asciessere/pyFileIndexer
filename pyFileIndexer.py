#!/usr/bin/env python3

import sys, os
import hashlib
import io, json

# performance timer
from timeit import default_timer as timer

# pyFileIndexer modules
import hashing
import duplicates

# GLOBALS
ENVVAR_JOB = "PFIDX_JOB"
ENVVAR_HASH = "PFIDX_HASH"
ENVVAR_PATH = "PFIDX_PATHS"


def print_flush(message):
    # print() nem sempre dá retorno imediato na tela
    # usando dessa forma pra monitorar melhor
    sys.stdout.write(message)
    sys.stdout.write('\n')
    sys.stdout.flush()


def get_envvar(varname):
    # get environment variable if it exists
    env_keys = os.environ.keys()

    if varname not in env_keys:
        # env var doesn't exist
        # TODO: throw error
        return ''
    else:
        return os.environ[varname]


##
# MAIN
##
def main():
    #

    # TYPE OF JOB
    job_arg = get_envvar(ENVVAR_JOB).upper()
    if job_arg == "HASHING":
        # do hashing
        paths_arg = get_envvar(ENVVAR_PATH)
        paths_list = paths_arg.split(',')

        hash_arg = get_envvar(ENVVAR_HASH).upper()
        hashing.set_hasher(hash_arg)

        start = timer()
        hashing.save_hashes(paths_list)
        end = timer()
        print_flush("HASHING: {} secs.".format(end - start))

    elif job_arg == "DUPES":
        # find duplicates
        dupes = duplicates.get_duplicates()

        # TODO: JSON output

    elif job_arg == "METADATA":
        # TODO: fill metadata
        print("... metadata job empty...")

    else:
        # no job defined
        print("Must specify job. Use PFIDX_JOB env var.")
        exit()


###################

if __name__ == "__main__":
    main()

