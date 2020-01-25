#!/bin/bash

export PATH=$PATH:/usr/local/opt/gettext/bin

# Update a .po file for i18n_test.py
xgettext -j -o i18n_test_ko.po i18n_test.py

# Update a .po file for i18n_multilang.py
# xgettext -j -o i18n_multilang_ko.po i18n_multilang.py
# xgettext -j -o i18n_multilang_zh.po i18n_multilang.py
# xgettext -j -o i18n_multilang_ja.po i18n_multilang.py
