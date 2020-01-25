#!/bin/bash

export PATH=$PATH:/usr/local/opt/gettext/bin

# Creates .po file for i18n_test.py
xgettext -d i18n_test_ko i18n_test.py

# Creates .po file for i18n_multilang.py
# xgettext -d i18n_multilang_ko i18n_multilang.py
# xgettext -d i18n_multilang_zh i18n_multilang.py
# xgettext -d i18n_multilang_ja i18n_multilang.py