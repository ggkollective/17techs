#!/usr/bin/python3

import datetime
import time

# t1 시간 기록 (특정 날짜)
t1 = datetime.datetime(
    year=2019, month=4, day=27, hour=13, minute=20, second=00)
# t1 시간 기록 (특정 날짜를 현재 시간을 기준으로 할 경우)
# t1 = datetime.datetime.now() + datetime.timedelta(minutes=1)

while True:
    now = datetime.datetime.now()
    print("현재 시간: {0}".format(now))
    print("루프 만료 시간: {0}".format(t1))
    if t1 <= now:
        break

    time.sleep(1)

