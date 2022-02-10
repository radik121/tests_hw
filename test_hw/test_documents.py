import unittest
from documents import list_all, add_all, delete
from unittest.mock import patch


class TestDoc(unittest.TestCase):
    docs = [{'type': 'passport', 'number': '25768', 'name': 'Иван Иванов'},
            {'type': 'passport', 'number': '166587', 'name': 'Петр Петров'},
            {'type': 'passport', 'number': '11-5286', 'name': 'Гарик Морзе'}
            ]

    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }

    # тест вывода списка документов
    def test_list_all(self):
        result = 'passport, 25768, Иван Иванов\npassport, 166587, Петр Петров\npassport, 11-5286, Гарик Морзе'
        self.assertEqual(list_all(self.docs), result)

    # тест добавления документа
    @patch('builtins.input', side_effect=['45678', 'passport', 'Арсений Крылов', '3'])
    def test_add_docs(self, mock_inputs):
        result = f"Вы добавили dict_values(['passport', '45678', 'Арсений Крылов']) на полку 3"
        self.assertEqual(add_all(self.docs, self.directories), result)

    @patch('builtins.input', side_effect=['45678'])
    def test_del_docs(self, mock_inputs):
        result = f"Вы удалили документ 45678"
        self.assertEqual(delete(self.docs, self.directories), result)