'''
this is the main file;
we run the app from here;
here we should find only the menu and no other implementation
'''

from services.user_service import UserService
from services.appointment_service import AppointmentService

def main_menu():
    print("\n--- Appointment Scheduling App ---")
    print("1. Add User")
    print("2. Delete User")
    print("3. List Users")
    print("4. Make an Appointment")
    print("5. View Appointments")
    print("6. Exit")
    return input("Choose an option: ")

def main():
    user_service = UserService()
    appointment_service = AppointmentService(user_service)

    while True:
        choice = main_menu()
        if choice == "1":
            user_service.add_user()
        elif choice == "2":
            user_service.delete_user()
        elif choice == "3":
            user_service.list_users()
        elif choice == "4":
            appointment_service.create_appointment()
        elif choice == "5":
            appointment_service.list_appointments()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_": main()