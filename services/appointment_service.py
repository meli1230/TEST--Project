from data.storage import appointments, consultants, available_slots, users  # import data lists for appointments, consultants, and users
from models.appointment import Appointment  # import the Appointment model
from utils.timezone import convert_to_timezone  # import a utility function for timezone conversion

# service class to handle appointment-related functionality
class AppointmentService:
    # constructor for the AppointmentService class
    def __init__(self, user_service):
        self.user_service = user_service  # initialize with a user service for user-related operations

    # method to create a new appointment
    def create_appointment(self):
        self.user_service.list_users()  # list all available users
        user_name = input("Enter user name: ").strip()  # prompt user for their name and remove extra spaces
        user = next((u for u in users if u.name.lower() == user_name.lower()), None)  # find user by name, case insensitive

        if not user:  # check if user is not found
            print("User not found. Please try again.")
            return

        print("Available Consultants:")
        for idx, consultant in enumerate(consultants, start=1):
            print(f"{idx}. {consultant}")

        try:
            consultant_choice = int(input("Choose consultant: ").strip())
            if consultant_choice < 1 or consultant_choice > len(consultants):
                raise ValueError
        except ValueError:
            print("Invalid consultant choice. Please try again.")
            return

        chosen_consultant = consultants[consultant_choice - 1]

        consultant_slots = available_slots.get(chosen_consultant, [])
        if not consultant_slots:
            print(f"No available slots for {chosen_consultant}.")
            return

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
            return

        chosen_slot = consultant_slots[slot_choice - 1]

        # Convert chosen slot to customer_time and mentor_time
        customer_time = chosen_slot  # assuming slot is already in customer's timezone
        mentor_time = convert_to_timezone(chosen_slot, "Customer_Timezone", "UTC")  # convert to a different timezone if needed

        appointment = Appointment(user=user, consultant=chosen_consultant, customer_time=customer_time, mentor_time=mentor_time)
        appointments.append(appointment)
        print("Appointment created successfully!")
