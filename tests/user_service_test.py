import unittest
from unittest.mock import patch, MagicMock
from services.user_service import UserService
from models.user import User
from data.storage import users

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService()
        users.clear()

    @patch('builtins.input', side_effect=['Utilizator test'])
    def test_add_user_valid_input(self, mock_input):
        self.service.add_user()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, 'Utilizator test')

    @patch('builtins.input', side_effect=['Utilizator test2'])
    def test_add_user_valid_name_2(self, mock_input):
        self.service.add_user()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, 'Utilizator test2')

    @patch('builtins.input', side_effect=['Utilizator test'])
    def test_delete_user_valid(self, mock_input):
        user = User(1, 'Utilizator test', '')
        users.append(user)
        self.service.delete_user()
        self.assertEqual(len(users), 0)

    @patch('builtins.input', side_effect=['Utilizator necunoscut'])
    def test_delete_user_notFound(self, mock_input):
        user = User(1, 'Utilizator test', '')
        users.append(user)
        with patch('builtins.print') as mock_print:
            self.service.delete_user()
            mock_print.assert_any_call('User not found.')
        self.assertEqual(len(users), 1)

    @patch('builtins.input', side_effect=['Utilizator test', 'Utilizator test2'])
    def test_add_multiple_users(self, mock_input):
        self.service.add_user()
        self.service.add_user()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, 'Utilizator test')
        self.assertEqual(users[1].name, 'Utilizator test2')

if __name__ == '__main__':
    unittest.main()
