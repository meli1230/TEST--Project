#from required modules and classes
from data.storage import users, TIMEZONES  #import the user data and timezone list
from models.user import User  #import the User model

#class to handle user-related functionality
class UserService:
    #method to add a new user
    def add_user(self):
        name = input("Enter user name: ")  #prompt the user to input their name

        print("Available Time Zones:")  #display available time zones
        for idx, tz in enumerate(TIMEZONES, 1):  #enumerate to display timezones with indices starting at 1
            print(f"{idx}. {tz}")

        try:
            tz_choice = int(input("Choose your timezone (enter the number): "))  #prompt the user to choose a timezone by index
            if tz_choice < 1 or tz_choice > len(TIMEZONES):  #validate the chosen timezone index
                raise ValueError("Invalid choice.")  #raise an error if the choice is invalid
            timezone = TIMEZONES[tz_choice - 1]  #assign the chosen timezone
        except Exception as e:
            print(f"Invalid input: {e}. Defaulting to UTC.")  #handle invalid input
            timezone = "UTC"  #default to UTC if input is invalid

        user_id = len(users) + 1  #generate a unique user ID
        user = User(user_id, name, timezone)  #create a new user instance
        users.append(user)  #add the new user to the users list
        print(f"User {name} added successfully with timezone {timezone}.")  #confirm successful user addition

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
