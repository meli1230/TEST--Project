from data.storage import appointments, consultants, available_slots, users  # import data lists for appointments, consultants, and users
from models.appointment import Appointment  # import the Appointment model
from utils.timezone import convert_to_timezone  # import a utility function for timezone conversion
import re  # import regular expressions module for input validation

# service class to handle appointment-related functionality
class AppointmentService:
    # constructor for the AppointmentService class
    def __init__(self, user_service):
        self.user_service = user_service  # initialize with a user service for user-related operations

    # method to create a new appointment
    def create_appointment(self):
        self.user_service.list_users()  # list all available users
        while True:
            user_name = input("Enter user name: ").strip()  # prompt user for their name and remove extra spaces
            if not re.match(r'^[a-zA-Z\u00C0-\u017F\s]+$', user_name):  # allow letters, spaces, and accented characters
                print("Invalid name. Please use only letters and spaces.")
                continue

            user = next((u for u in users if u.name.lower() == user_name.lower()), None)  # find user by name, case insensitive
            if not user:  # check if user is not found
                print("User not found. Please try again.")
                return
            break

        while True:  # Loop only for consultant selection
            print("Available Consultants:")
            for idx, consultant in enumerate(consultants, start=1):
                print(f"{idx}. {consultant}")

            try:
                consultant_choice = int(input("Choose consultant: ").strip())
                if consultant_choice < 1 or consultant_choice > len(consultants):
                    raise ValueError
            except ValueError:
                print("Invalid consultant choice. Please try again.")
                continue  # Restart consultant selection

            chosen_consultant = consultants[consultant_choice - 1]
            break  # Exit loop on valid choice

        consultant_slots = available_slots.get(chosen_consultant, [])
        if not consultant_slots:
            print(f"No available slots for {chosen_consultant}.")
            return

        while True:
            print("Available slots:")
            for idx, slot in enumerate(consultant_slots, start=1):
                print(f"{idx}. {slot}")

            try:
                slot_choice = input("Choose a slot: ").strip()
                if not slot_choice.isdigit():
                    raise ValueError("Slot choice must be a number.")

                slot_choice = int(slot_choice)
                if slot_choice < 1 or slot_choice > len(consultant_slots):
                    raise ValueError("Slot choice out of range.")
            except ValueError as e:
                print(f"Invalid slot choice: {e}. Please try again.")
                continue  # Restart slot selection

            chosen_slot = consultant_slots[slot_choice - 1]
            break  # Exit loop on valid slot choice

        # Convert chosen slot to customer_time and mentor_time
        customer_time = chosen_slot  # assuming slot is already in customer's timezone
        mentor_time = convert_to_timezone(chosen_slot, "Customer_Timezone", "UTC")  # convert to a different timezone if needed

        # Remove the chosen slot from available slots for the chosen consultant
        available_slots[chosen_consultant].remove(chosen_slot)

        appointment = Appointment(user=user, consultant=chosen_consultant, customer_time=customer_time, mentor_time=mentor_time)
        appointments.append(appointment)
        print("Appointment created successfully!")

    # method to list all appointments
    def list_appointments(self):
        if not appointments:
            print("No appointments scheduled.")
            return

        print("Scheduled Appointments:")
        for idx, appointment in enumerate(appointments, start=1):
            print(f"{idx}. User: {appointment.user.name}, Consultant: {appointment.consultant}, Time: {appointment.customer_time}")
