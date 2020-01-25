#!/usr/bin/python3

import hashlib
import time


def computeMD5(str):
    hasher = hashlib.md5()
    hasher.update(str.encode('utf-8'))
    return hasher.hexdigest()


def computeSHA512(str):
    hasher = hashlib.sha512()
    hasher.update(str.encode('utf-8'))
    return hasher.hexdigest()


# 백만 개의 MD5 해시 생성 속도를 측정합니다.
md5_t1 = time.monotonic()
for i in range(1, 1000000):
    computeMD5(str('hash_test_key_{0}'.format(i)))

md5_t2 = time.monotonic()

# 백만 개의 SHA-512 해시 생성 속도를 측정합니다.
sha2_t1 = time.monotonic()
for i in range(1, 1000000):
    computeSHA512(str('hash_test_key_{0}'.format(i)))

sha2_t2 = time.monotonic()

print("Elapsed time(MD5)={0}".format(md5_t2-md5_t1))
print("Elapsed time(SHA-512)={0}".format(sha2_t2-sha2_t1))