
import sys

#pyFileIndexer modules
import db


def get_duplicates():

    dupes = {}

    keys = db.get_duplicate_hashes()
    for k in keys:
        dupes[k] = db.get_files(k.decode())

        # TEST PRINT
        print("HASH: {}".format(k.decode()))
        for f in dupes[k]:
            print(f)

    return dupes

