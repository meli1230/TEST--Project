from data.storage import users
from models.user import User

class UserService:
    def add_user(self):
        name = input("Enter user name: ")
        timezone = input("Enter your timezone (e.g., 'UTC', 'CET'): ")
        user_id = len(users) + 1
        user = User(user_id, name, timezone)
        users.append(user)
        print(f"User {name} added successfully.")

    def delete_user(self):
        self.list_users()
        user_id = int(input("Enter user ID to delete: "))
        for user in users:
            if user.user_id == user_id:
                users.remove(user)
                print(f"User {user.name} deleted successfully.")
                return
        print("User not found.")

    def list_users(self):
        if not users:
            print("No users found.")
            return
        for user in users:
            print(f"ID: {user.user_id}, Name: {user.name}, Timezone: {user.timezone}")
