
import os
import hashlib

# pyFileIndexer modules
import db

# DEFAULT HASH
_hasher_name = 'SHA1' # used as default


def set_hasher(hasher_name):
    global _hasher_name

    if hasher_name != '':
        _hasher_name = hasher_name


def get_hash(filepath):

    block_size = 4096

    if _hasher_name == 'MD5':
        hasher = hashlib.md5()
    elif _hasher_name == 'SHA1':
        hasher = hashlib.sha1()
    elif _hasher_name == 'SHA256':
        hasher = hashlib.sha256()
    else:
        print("No hashlib defined. Use PFIDX_HASH environment variable.")
        exit()

    with open(filepath, 'rb') as f:
        data = f.read(block_size)
        while len(data) > 0:
            hasher.update(data)
            data = f.read(block_size)

    return hasher.hexdigest()


def save_hashes(paths):
    for p in paths:
        files = []
        for r,d,f in os.walk(p):
            for filename in f:
                files.append(os.path.join(r,filename))

        for f in files:
            h = get_hash(f)
            print("save_hash({}, {})".format(h,f))
            db.save_hash(h, f)


