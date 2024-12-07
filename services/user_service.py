from data.storage import users, TIMEZONES
from models.user import User


class UserService:
    def add_user(self):
        name = input("Enter user name: ")
        print("Available Time Zones:")
        for idx, tz in enumerate(TIMEZONES, 1):
            print(f"{idx}. {tz}")

        try:
            tz_choice = int(input("Choose your timezone (enter the number): "))
            if tz_choice < 1 or tz_choice > len(TIMEZONES):
                raise ValueError("Invalid choice.")
            timezone = TIMEZONES[tz_choice - 1]
        except Exception as e:
            print(f"Invalid input: {e}. Defaulting to UTC.")
            timezone = "UTC"

        user_id = len(users) + 1
        user = User(user_id, name, timezone)
        users.append(user)
        print(f"User {name} added successfully with timezone {timezone}.")

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

