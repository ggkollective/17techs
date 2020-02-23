#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 protobuf3, six 모듈이 필요합니다.

from . import oneof_message_pb2


def create_login():
    new_req = oneof_message_pb2.RequestMsg()
    new_req.login.user_id = "gigone.lee@gmail.com"
    new_req.login.password = "p@ssw0rd"
    return new_req


def create_order():
    new_req = oneof_message_pb2.RequestMsg()
    new_req.order.access_token = "1a2s3d4f5g6h7j8k9l"
    return new_req


def create_refund():
    new_req = oneof_message_pb2.RequestMsg()
    new_req.refund.access_token = "1a2s3d4f5g6h7j8k9l"
    return new_req


requests = [create_login(), create_order(), create_refund()]
for req in requests:
    req_type = req.WhichOneof('msg')
    if req_type == 'login':
        print('req_type is Login: id={0}'.format(req.login.user_id))
    elif req_type == 'order':
        print('req_type is Order: token={0}'.format(req.order.access_token))
    elif req_type == 'refund':
        print('req_type is Refund: token={0}'.format(req.refund.access_token))
    else:
        assert False  # 정의되지 않은 요청 타입




