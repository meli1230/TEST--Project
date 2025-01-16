#from required modules and classes
from data.storage import users, TIMEZONES  #import the user data and timezone list
from models.user import User  #import the User model
import re

#class to handle user-related functionality
import re  # Import regex module for name validation

class UserService:
    # Method to add a new user
    def add_user(self):
        # Prompt the user to input their name
        name = input("Enter user name: ").strip()

        # Validate the name: only allow alphabetic characters and spaces
        if not re.match("^[A-Za-z0-9 _@!#$%^&*()+=-]+$", name):
            print("Invalid name. Names should not contain numbers or special characters.")
            return  # Exit the method if the name is invalid

        # Display available time zones for selection
        print("Available Time Zones:")
        for idx, tz in enumerate(TIMEZONES, 1):  # Enumerate timezones for better readability
            print(f"{idx}. {tz}")

        # Prompt the user to select their timezone
        try:
            tz_choice = int(input("Choose your timezone (enter the number): "))
            if tz_choice < 1 or tz_choice > len(TIMEZONES):  # Validate the timezone choice
                raise ValueError("Invalid choice.")
            timezone = TIMEZONES[tz_choice - 1]  # Map the choice to the corresponding timezone
        except Exception as e:  # Handle invalid inputs gracefully
            print(f"Invalid input: {e}. Defaulting to UTC.")  # Inform the user and default to UTC
            timezone = "UTC"  # Assign default timezone if input is invalid

        # Generate a unique user ID and create the new user
        user_id = len(users) + 1
        user = User(user_id, name, timezone)  # Create a new User instance
        users.append(user)  # Add the new user to the users list

        # Confirm successful user addition
        print(f"User {name} added successfully with timezone {timezone}.")

    #method to delete a user
    def delete_user(self):
        self.list_users_when_delete()  #list all users for selection during deletion
        username = input("Enter user name to delete: ")  #prompt the user to input the name of the user to delete
        for user in users:  #iterate through the list of users
            if user.name == username:  #check if the current user matches the input name
                users.remove(user)  #remove the user from the list
                print(f"User {user.name} deleted successfully.")  #confirm successful deletion
                return  #exit the function after deletion
        print("User not found.")  #notify if the user is not found

    #method to list all users
    def list_users(self):
        if not users:  #check if there are no users
            print("No users found.")  #notify if no users are found
            return  #exit the function
        for user in users:  #iterate through the list of users
            print(f"ID: {user.user_id}, Name: {user.name}, Timezone: {user.timezone}")  #display user details

    #method to list users for deletion
    def list_users_when_delete(self):
        if not users:  #check if there are no users
            print("No users found.")  #notify if no users are found
            return  #exit the function
        for user in users:  #iterate through the list of users
            print(f"Name: {user.name}, Timezone: {user.timezone}")  #display user details
