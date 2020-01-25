#!/usr/bin/python3

import uuid


for i in range(1, 5):
    print('랜덤 UUID({0})={1}'.format(i, uuid.uuid4()))
