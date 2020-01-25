#!/bin/bash

export PATH=$PATH:/usr/local/opt/gettext/bin

# Creates MO file
msgfmt ./i18n_test_ko.po -o ./locale/ko_KR/LC_MESSAGES/i18n_test.mo
# Executes i18n_test.py
python3 i18n.py

# msgfmt ./i18n_multilang_ko.po -o ./locale/ko_KR/LC_MESSAGES/i18n_multilang.mo
# msgfmt ./i18n_multilang_zh.po -o ./locale/zh_CN//LC_MESSAGES/i18n_multilang.mo
# msgfmt ./i18n_multilang_ja.po -o ./locale/ja_JP/LC_MESSAGES/i18n_multilang.mo
# python3 i18n_multilang.py