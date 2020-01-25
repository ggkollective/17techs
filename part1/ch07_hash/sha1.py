#!/usr/bin/python3

import hashlib


def computeSHA1(str):
    hasher = hashlib.sha1()
    hasher.update(str.encode('utf-8'))
    return hasher.hexdigest()


hash1 = computeSHA1('해시 값 1')
hash2 = computeSHA1('해시 값 2')

print('해시 값1={0} / 길이={1}'.format(hash1, len(hash1)))
print('해시 값2={0} / 길이={1}'.format(hash2, len(hash2)))
