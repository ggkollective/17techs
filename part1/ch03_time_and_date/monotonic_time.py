#!/usr/bin/python3

import time


# t1 시간 기록 (현재)
t1 = time.monotonic()

while True:
    # t2 시간 기록
    t2 = time.monotonic()
    # 이 루프가 3초 이상 실행된 경우 종료합니다.
    if t2 >= t1 + 3:
        break

    time.sleep(0.1)

# 실제 시간 차이를 출력합니다.
print("t1={0}".format(t1))
print("t2={0}".format(t2))
print("diff={0}".format(t2-t1))
