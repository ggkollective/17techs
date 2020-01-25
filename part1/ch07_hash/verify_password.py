#!/usr/bin/python3

import hashlib

hash_map = {}


def computeSHA256(str):
    hasher = hashlib.sha256()
    # 해시 함수 알고리즘을 알아도 비밀번호를 유추할 수 없게 salt 값을 추가합니다.
    hasher.update((str + 'my_salt').encode('utf-8'))
    return hasher.hexdigest()


while True:
    print('ID를 입력하세요: ')
    user_id = input()
    print('비밀번호를 입력하세요: ')
    password = input()
    if user_id in hash_map:
        if hash_map[user_id] == computeSHA256(password):
            print('{0}: 비밀번호가 일치합니다.'.format(user_id))
        else:
            print('{0}: 비밀번호가 일치하지 않습니다.'.format(user_id))
    else:
        hash_map[user_id] = computeSHA256(password)
        print('{0}: 비밀번호를 설정했습니다.'.format(user_id))
