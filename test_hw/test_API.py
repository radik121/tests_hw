import pytest
from Yandex_API_file import YaAPI


# Необходим файл ya.token.txt с токеном внутри
# Тест на проверку ответа 201.
def test_create_folder():
    a = YaAPI()
    assert a.create_folder('netology') == 201


# Тест проверят наличие папки на диске
def test_check_folder():
    a = YaAPI()
    assert a.check_folder('netology') == 200