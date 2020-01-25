import json

# 유니코드 문자열을 명시하기 위해 u를 붙였습니다.
message2 = {
    u'number': 12345,
    u'pi': 3.14,
    u'str': u'문자열 값',
    u'null_key': None,
    u'object': {
        u'str2': u'문자열 값 2',
        u'object2': {
            u'number2': 12345
        }
    },
    u'num_array': [1, 2, 3, 4, 5],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}

# ensure_ascii=True 인 경우에는 아스키 코드가 아닌 모든 문자열을 \uXXXX 로 표기합니다.
with open('message2.json', 'w', encoding='UTF8') as file:
    json.dump(message2, file, ensure_ascii=False)
    # 들여쓰기 추가
    # json.dump(message2, file, ensure_ascii=False, indent=2)
    # 키 정렬까지 필요한 경우
    # json.dump(message2, file, ensure_ascii=False, indent=2, sort_keys=True)
