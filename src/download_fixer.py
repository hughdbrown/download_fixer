#!/usr/bin/env python
from __future__ import print_function

from hashlib import sha1
from collections import defaultdict
import os.path
import os


def calc_sha(filename, size=256 * 1000 * 1000):
    """
    Calculate the sha1 hash of a file. Read in blocks.
    """
    sh = sha1()
    with open(filename, "rb") as f:
        while True:
            s = f.read(size)
            if not s:
                break
            sh.update(s)
        return sh.hexdigest()


def fullpathiter(startdir):
    return [
        os.path.normpath(os.path.join(root, f))
        for root, _, files in os.walk(startdir)
        for f in files
    ]


def main(startdir='.'):
    def fn(filename):
        # All arguments that are file names or paths
        # in a format statement have to have single quotes
        # escaped so that the python single quotes
        # enclosing are not terminated unsyntactically.
        return filename.replace("'", r"\'")
    d = defaultdict(list)
    for fullpath in fullpathiter(startdir):
        if not os.path.islink(fullpath):
            file_hash = calc_sha(fullpath)
            d[file_hash].append({
                'name': fullpath,
            })
    for key, values in d.items():
        if len(values) > 1:
            print('# ', '-' * 30, key)
            # Split into original and duplicates
            original, duplicates = (
                values[0]['name'],
                [x['name'] for x in values[1:]]
            )
            old_filename = os.path.split(original)[1]
            # Give the duplicate file a name in the storage directory
            # so that different files of that name in different
            # directories could be linked in the storage directory.
            new_filename = "{0}-{1}".format(key, old_filename)
            new_filepath = os.path.join("data", new_filename)
            # Delete the duplicates first.
            # Has the beneficial side effect of freeing up space,
            # making it possible to create a directory in the next step.
            for duplicate in duplicates:
                print(
                    "rm '{0}'".
                    format(fn(duplicate))
                )
            # Make a storage directory to store file
            print("mkdir -p data")
            # Move the single existing copy to the storage directory
            print(
                "mv '{0}' '{1}'".
                format(fn(original), fn(new_filepath))
            )
            # Link all the former copies to the renamed file
            # in the storage directory
            for duplicate in [original] + duplicates:
                linked_dir = os.path.split(duplicate)[0]
                linked_filepath = os.path.join(linked_dir, old_filename)
                print(
                    "ln -s '{0}' '{1}'".
                    format(fn(new_filepath), fn(linked_filepath))
                )
            print('# ', '-' * 30)


if __name__ == '__main__':
    fixer('.')
