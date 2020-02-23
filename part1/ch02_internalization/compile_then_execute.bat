:: Creates MO file
msgfmt64.exe i18n_test_ko.po -o locale\ko_KR\LC_MESSAGES\i18n_test.mo
:: Executes i18n_test.py
python.exe i18n_test.py

msgfmt64.exe i18n_multilang_ko.po -o locale\ko_KR\LC_MESSAGES\i18n_multilang.mo
msgfmt64.exe i18n_multilang_zh.po -o locale\zh_CN\LC_MESSAGES\i18n_multilang.mo
msgfmt64.exe i18n_multilang_ja.po -o locale\ja_JP\LC_MESSAGES\i18n_multilang.mo
python.exe i18n_multilang.py