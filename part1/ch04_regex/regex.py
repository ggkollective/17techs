#!/usr/bin/python3

import re


def find_pattern(pattern, string):
    match = re.findall(pattern, string)
    if not match:
        print("일치하는 데이터가 없습니다.")
        return

    print("일치하는 데이터를 찾았습니다: {0}".format(match))


# 특정 문자 1개를 찾는 코드
find_pattern('o', 'Hello World')
# 소문자를 찾는 함수 호출 코드
find_pattern('[a-z]', 'Hello World, 1,2,3,4,5')
# 대문자를 찾는 함수 호출 코드
find_pattern('[A-Z]', 'Hello World, 1,2,3,4,5')
# 대소문자를 모두 찾는 함수 호출 코드
find_pattern('[a-zA-Z]', 'Hello World, 1,2,3,4,5')
# 숫자 1개만 찾는 함수 호출 코드
find_pattern('[0-9]', 'Hello World, 1,2,3,4,5')
# 대소 문자 또는 숫자 1개를 찾는 함수 호출 코드
find_pattern('[a-zA-Z0-9]', 'Hello World, 1,2,3,4,5')
# 파이썬 언어는 문자옆 앞에 r을 붙여 다음과 같이 \ 파싱을 피할 수 있습니다.
# find_pattern(r'[\\\[\]]', r'!@#$%^&*()?><\[]')과 같습니다.
find_pattern('[\\\\\\[\\]]', '!@#$%^&*()?><\\[]')
# 소문자 문자열을 찾는 함수 호출 코드
find_pattern('[a-z]+', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')
# 글자 수가 3개인 문자열을 찾는 함수 호출 코드
find_pattern('[a-z0-9,]{3}', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')
# 최소 3글자, 최대 5글자의 문자열을 찾는 함수 호출 코드
find_pattern('[a-z0-9,]{3,5}', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')
# 첫 3글자가 소문자 또는 대문자인지 검사하는 코드
find_pattern('^[a-zA-Z]{3}', r'Hello World, 1,2,3,4,5, !@#$%^&*()?></\[]')
# 마지막 3글자가 소문자, 대문자, 숫자가 아닌지 (특수문자인지) 검사하는 코드
find_pattern('[^a-z^A-Z^0-9]{3}$', r'Hello World, 1,2,3,4,5,!@#$%^&*()?></\[]')
