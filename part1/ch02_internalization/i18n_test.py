#!/usr/bin/python3
# 다음 코드를 실행하기 위해서는 python-gettext 모듈이 필요합니다.
import gettext


translation_ko = gettext.translation(
    domain='i18n_test', localedir='./locale', languages=['ko_KR'])


translation_ko.install()

print(_('Test message 1'))
print('Test message 2')
print(_('Test message 3'))

# http://www.labri.fr/perso/fleury/posts/programming/a-quick-gettext-tutorial.html
