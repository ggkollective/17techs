#!/usr/bin/python3

import datetime

# 시스템 기본 시간
t1 = datetime.datetime.now()
# UTC 시간
t2 = datetime.datetime.now(tz=datetime.timezone.utc)

print("시스템 기본 시간: {0}".format(t1))
print("UTC 시간: {0}".format(t2))
