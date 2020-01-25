#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 lxml 모듈이 필요합니다.

from lxml import etree


def read_xpath(tree, xpath):
    tags = tree.xpath(xpath)
    if tags and len(tags) > 0:
        return True, tags[0]
    else:
        return False, None


def read_all(tree, xpath):
    for tag in tree:
        if len(tag) > 0:
            # 객체 또는 배열 요소인 경우
            read_all(tag, '{0}/{1}'.format(xpath, tag.tag))
        else:
            if tag.text:
                print('{0}/{1}={2}'.format(xpath, tag.tag, tag.text))
            else:
                print('{0}/{0}'.format(xpath, tag.tag))


def open_xml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return etree.parse(file)
        except KeyError as e:
            print('XML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


# message1.xml 파일은 같은 디렉토리에 있어야 합니다.
xml_tree = open_xml_file('message1.xml')
if not xml_tree:
    # 더 이상 로직을 진행할 수 없으므로 종료합니다.
    exit(0)

#
# Iterator 기반 접근
exist, root_tree = read_xpath(xml_tree, '/message')
assert exist
read_all(root_tree, root_tree.tag)
