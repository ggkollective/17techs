#!/usr/bin/python3

import random


# 랜덤값을 10번 출력합니다.
for i in range(1, 10):
    # seed 값을 현재 시간(타임스탬프)로 설정합니다.
    random.seed(0)
    print(random.randrange(1, 10))
