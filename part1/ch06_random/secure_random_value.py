#!/usr/bin/python3

import os
import struct

# 랜덤 값을 10번 출력합니다.
for i in range(1, 10):
    # 운영체에서 제공하는 기능을 사용해 랜덤하게 생성된 4바이트 값을 읽습니다.
    random_four_byte = os.urandom(4)
    # 4바이트 값을 정수로 변환한 후, 출력합니다.
    random_integer = struct.unpack("<L", random_four_byte)[0]
    print('hex=' + random_four_byte.hex() + ", integer=" + str(random_integer))
