#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 lxml 모듈이 필요합니다.

from lxml import etree

message2 = {
    u'number': u'12345',
    u'pi': u'3.14',
    u'str': u'문자열 값',
    u'null_tag': None,
    u'object': {
        u'str2': u'문자열 값 2',
        u'object2': {
            u'number2': u'12345'
        }
    },
    u'num_array': [u'1', u'2', u'3', u'4', u'5'],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}


def to_xml(tree, dict_object):
    for key in dict_object:
        element = etree.SubElement(tree, key)
        value = dict_object[key]
        if value:
            # 키에 대한 값이 존재하는 경우 값의 타입을 확인한 후 처리합니다.
            if type(value) is str:
                # dict 값이 단순 문자열인 경우 값만 추가합니다.
                element.text = value
            elif type(value) is dict:
                # dict 값이 또 다른 dict 객체인 경우 이 함수를 재귀적으로 호출합니다.
                to_xml(element, value)
            elif type(value) is list:
                # dict 값이 리스트인 경우 리스트를 순회하며 값을 추가합니다.
                for v in value:
                    assert type(v) is str
                    etree.SubElement(element, 'element').text = v
            else:
                # XML 에서 지원하지 않는 타입이 있습니다.
                assert False
        else:
            # 키에 대한 값이 존재하지 않는 경우 키만 등록합니다.
            pass


xml_tree = etree.Element('message')
to_xml(xml_tree, message2)

with open('message2.xml', 'wb') as file:
    file.write(etree.tostring(
        xml_tree, xml_declaration=True, encoding='UTF-8', pretty_print=True))

