#!/usr/bin/python3

import random
import time
import os

# 유사 난수 값을 백만 번 생성한 후, 성능을 측정합니다.
random.seed()
prng_t1 = time.monotonic()
for i in range(1, 1000000):
    random.random()

prng_t2 = time.monotonic()

# 암호학적으로 안전한 난수 값을 백만 번 생성한 후, 성능을 측정합니다.
srng_t1 = time.monotonic()
for i in range(1, 1000000):
    random_four_byte = os.urandom(4)

srng_t2 = time.monotonic()

print("Elapsed time(PRNG)={0}".format(prng_t2-prng_t1))
print("Elapsed time(SRNG)={0}".format(srng_t2-srng_t1))