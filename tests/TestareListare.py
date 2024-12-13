import unittest
from unittest.mock import MagicMock
from services.user_service import UserService


class TestareListare(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.user_service.list_users = MagicMock(return_value=["John Doe", "Jane Smith"])

    def test_list_users(self):
        users = self.user_service.list_users()
        self.user_service.list_users.assert_called_once()
        self.assertEqual(len(users), 2)
        self.assertIn("John Doe", users)


if __name__ == "__main__":
    unittest.main()
