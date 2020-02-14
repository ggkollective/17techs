#!/usr/bin/python3

import re


def check_password(password):
    # len(password) >= 8 코드로도 검사할 수 있습니다.
    result = re.search(r'.{8,}', password)
    if not result:
        print("최소 8글자 이상이어야 합니다.")
        return

    print(password)
    result = re.search(r'[a-z]+', password)
    if not result:
        print("최소 1개 이상의 소문자가 필요합니다.")
        return

    result = re.search(r'[A-Z]+', password)
    if not result:
        print("최소 1개 이상의 대문자가 필요합니다.")
        return

    result = re.search(r'[0-9]+', password)
    if not result:
        print("최소 1개 이상의 숫자가 필요합니다.")
        return

    result = re.search(r'[@#$%^&+=]', password)
    if not result:
        print("최소 1개의 특수 문자(@#%^&+=)를 포함해야 합니다.")
        return

    print("비밀번호 검증에 성공했습니다.")


check_password('<Your password@>')
