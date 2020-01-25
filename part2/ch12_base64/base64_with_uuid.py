#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 별도 모듈이 필요하지 않습니다.

import base64
import uuid


my_uuid = uuid.uuid4()
print('원본 UUID={0}, 바이트 길이={1}'.format(str(my_uuid), len(my_uuid.bytes)))
b64_encoded_str = base64.b64encode(my_uuid.bytes)
print('base64 인코딩 문자열=\'{0}\', 바이트 길이={1}'.format(
    b64_encoded_str.decode('utf-8'), len(b64_encoded_str)))


decoded_uuid = uuid.UUID(bytes=base64.b64decode(b64_encoded_str))
print('base64 디코딩 된 UUID={0}'.format(decoded_uuid))
