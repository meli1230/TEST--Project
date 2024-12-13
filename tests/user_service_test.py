#import required modules and classes for testing
import unittest  #import the unittest module for unit testing
from unittest.mock import patch, MagicMock  #import patch and MagicMock for mocking methods and inputs
from services.user_service import UserService  #import the UserService class
from models.user import User  #import the User model
from data.storage import users  #import the users storage list

#test class for UserService functionality
class TestUserService(unittest.TestCase):
    def setUp(self):  #setup method to initialize test dependencies
        self.service = UserService()  #create an instance of UserService
        users.clear()  #clear the users list to ensure a clean test environment

    @patch('builtins.input', side_effect=['Utilizator test'])  #mock input to simulate user input
    def test_add_user_valid_input(self, mock_input):  #test method for adding a user with valid input
        self.service.add_user()  #call the add_user method
        self.assertEqual(len(users), 1)  #assert that one user has been added
        self.assertEqual(users[0].name, 'Utilizator test')  #assert that the user's name matches the input

    @patch('builtins.input', side_effect=['Utilizator123'])  #mock input with a name containing numbers
    def test_add_user_invalidNameNumbers(self, mock_input):  #test method for adding a user with invalid input (numbers)
        self.service.add_user()  #call the add_user method
        self.assertEqual(len(users), 0)  #assert that no user has been added

    @patch('builtins.input', side_effect=['Utilizator@Special'])  #mock input with a name containing special characters
    def test_add_user_invalidNameSpecialChars(self, mock_input):  #test method for adding a user with invalid input (special characters)
        self.service.add_user()  #call the add_user method
        self.assertEqual(len(users), 0)  #assert that no user has been added

    @patch('builtins.input', side_effect=['Utilizator test'])  #mock input to simulate a valid user deletion
    def test_delete_user_valid(self, mock_input):  #test method for deleting an existing user
        user = User(1, 'Utilizator test', '')  #create a user instance
        users.append(user)  #add the user to the list
        self.service.delete_user()  #call the delete_user method
        self.assertEqual(len(users), 0)  #assert that the user has been removed

    @patch('builtins.input', side_effect=['Utilizator necunoscut'])  #mock input for a nonexistent user
    def test_delete_user_notFound(self, mock_input):  #test method for attempting to delete a nonexistent user
        user = User(1, 'Utilizator test', '')  #create a user instance
        users.append(user)  #add the user to the list
        with patch('builtins.print') as mock_print:  #mock the print function
            self.service.delete_user()  #call the delete_user method
            mock_print.assert_any_call('User not found.')  #assert that the correct message was printed
        self.assertEqual(len(users), 1)  #assert that no user was removed

    @patch('builtins.input', side_effect=['Utilizator test', 'Utilizator test2'])  #mock input for adding multiple users
    def test_add_multiple_users(self, mock_input):  #test method for adding multiple users
        self.service.add_user()  #call the add_user method for the first user
        self.service.add_user()  #call the add_user method for the second user
        self.assertEqual(len(users), 2)  #assert that two users have been added
        self.assertEqual(users[0].name, 'Utilizator test')  #assert that the first user's name matches the input
        self.assertEqual(users[1].name, 'Utilizator test2')  #assert that the second user's name matches the input

if __name__ == '__main__':  #run the tests if the script is executed directly
    unittest.main()  #run all the test cases
