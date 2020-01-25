#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 protobuf3, six 모듈이 필요합니다.

import pbuf_message_pb2  # noqa: E402


def create_message():
    new_msg = pbuf_message_pb2.ProtobufMessage()
    new_msg.number = 12345
    new_msg.pi = 3.14
    new_msg.str = u'문자열 값'
    new_msg.object.str2 = u'문자열 값2'
    new_msg.object.object2.number2 = 12345
    for i in range(5):
        new_msg.num_array.append(i)
    new_msg.str_array.append(u'one')
    new_msg.str_array.append(u'two')
    new_msg.str_array.append(u'three')
    new_msg.str_array.append(u'four')
    new_msg.str_array.append(u'five')

    return new_msg


pbuf_message = create_message()
# print(pbuf_message)

with open('message2.dat', 'wb') as file:
    file.write(pbuf_message.SerializeToString())

with open('message2.dat', 'rb') as file:
    pbuf_message = pbuf_message_pb2.ProtobufMessage()
    pbuf_message.ParseFromString(file.read())
    print(pbuf_message)
