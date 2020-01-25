#!/usr/bin/python3

import hashlib


def computeSHA256(str):
    hasher = hashlib.sha256()
    hasher.update(str.encode('utf-8'))
    return hasher.hexdigest()


def computeSHA512(str):
    hasher = hashlib.sha512()
    hasher.update(str.encode('utf-8'))
    return hasher.hexdigest()


hash1 = computeSHA256('해시 값 1')
hash2 = computeSHA256('해시 값 2')
hash3 = computeSHA512('해시 값 1')
hash4 = computeSHA512('해시 값 2')

print('해시 값1={0} / 길이={1}'.format(hash1, len(hash1)))
print('해시 값2={0} / 길이={1}'.format(hash2, len(hash2)))
print('해시 값3={0} / 길이={1}'.format(hash3, len(hash3)))
print('해시 값4={0} / 길이={1}'.format(hash4, len(hash4)))
