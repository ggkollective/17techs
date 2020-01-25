#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 protobuf3, six 모듈이 필요합니다.

import simple_message_pb2
import uuid


def create_new_msg():
    new_msg = simple_message_pb2.SimpleMessage()
    new_msg.name = u'문자열'
    new_msg.num64 = 12345
    new_msg.float64 = 12345.6
    new_uuid = uuid.uuid4()
    print('new_uuid={0}'.format(new_uuid))
    new_msg.uuid = new_uuid.bytes
    # enum type
    new_msg.type = simple_message_pb2.SimpleMessage.Ping
    # number list
    new_msg.num64_list.append(1)
    new_msg.num64_list.append(2)
    # string list
    new_msg.name_list.append(u'one')
    new_msg.name_list.append(u'two')
    # map
    new_msg.map_field['key1'] = u'value1'
    new_msg.map_field['key2'] = u'value2'
    # Another message
    new_msg.another_msg.name = u'문자열2'
    new_msg.another_msg.num64 = 56789

    for i in range(5):
        another_msg2 = simple_message_pb2.AnotherMessage()
        another_msg2.name = u'문자열-{0}'.format(i)
        another_msg2.num64 = i
        new_msg.another_msg2.append(another_msg2)

    return new_msg


simple_message = create_new_msg()
print('------------------------------------------------------------------')
# 빈 문자열은 ' ', 정수나 실수는 0으로 표기됩니다.
print('name={0}'.format(simple_message.name))
print('num64={0}'.format(simple_message.num64))
print('float64={0}'.format(simple_message.float64))
print('uuid={0}'.format(str(uuid.UUID(bytes=simple_message.uuid))))

index = 0
for num64 in simple_message.num64_list:
    print('num64_list[{0}].num64={1}'.format(index, num64))
    index += 1

index = 0
for name in simple_message.name_list:
    print('name_list[{0}].num64={1}'.format(index, name))
    index += 1

print('type={0}'.format(simple_message.type))

for key in simple_message.map_field:
    print('map_field[{0}]={1}'.format(key, simple_message.map_field[key]))

another_msg = simple_message.another_msg
print('another_msg.name={0}'.format(another_msg.name))
print('another_msg.num64={0}'.format(another_msg.num64))

index = 0
for msg2 in simple_message.another_msg2:
    print('another_msg[{0}].name={1}, num64={2}'.format(
        index, msg2.name, msg2.num64))
    index += 1

print('------------------------------------------------------------------')

# Protobuf to text
from google.protobuf import text_format
text_message = text_format.MessageToString(simple_message, as_utf8=True)
print(text_message)

# Protobuf to JSON
from google.protobuf import json_format
import json
json_str = json_format.MessageToJson(simple_message)
print(json.loads(json_str))

import base64
object2 = json.loads(json_str)
decoded_uuid = uuid.UUID(bytes=base64.b64decode(object2['uuid']))
print(decoded_uuid)
