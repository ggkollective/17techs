#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 lxml 모듈이 필요합니다.

from lxml import etree


def open_xml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return etree.parse(file, parser=etree.XMLParser(encoding='utf-8'))
        except KeyError as e:
            print('XML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


# message1.xml 파일은 같은 디렉토리에 있어야 합니다.
xml_tree = open_xml_file('message1.xml')
if xml_tree:
    print(etree.tounicode(xml_tree, pretty_print=True))
