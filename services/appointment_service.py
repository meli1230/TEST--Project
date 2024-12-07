from data.storage import appointments, consultants
from models.appointment import Appointment
from utils.timezone import convert_to_timezone

class AppointmentService:
    def __init__(self, user_service):
        self.user_service = user_service

    def create_appointment(self):
        self.user_service.list_users()
        user_id = int(input("Enter user ID: "))
        user = next((u for u in users if u.user_id == user_id), None)
        if not user:
            print("User not found.")
            return

        print("Available Consultants:")
        for idx, consultant in enumerate(consultants, 1):
            print(f"{idx}. {consultant}")
        consultant_idx = int(input("Choose consultant: ")) - 1
        if consultant_idx not in range(len(consultants)):
            print("Invalid choice.")
            return
        consultant = consultants[consultant_idx]

        datetime = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
        local_time = convert_to_timezone(datetime, user.timezone)

        appointment = Appointment(user, consultant, local_time)
        appointments.append(appointment)
        print("Appointment created successfully.")

    def list_appointments(self):
        if not appointments:
            print("No appointments scheduled.")
            return
        for appt in appointments:
            print(appt)
