from Database.database import appointments_table
from data.storage import appointments, consultants, available_slots  # Eliminat lista `users`
from models.appointment import Appointment  # Import the Appointment model
from utils.timezone import convert_to_timezone  # Import a utility function for timezone conversion
from Database.database import list_users as db_list_users  # Import list_users direct din baza de date

# Service class to handle appointment-related functionality
class AppointmentService:
    # Constructor for the AppointmentService class
    def __init__(self, appointments_table, user_service):
        self.appointments_table = appointments_table  # Store the appointments table
        self.user_service = user_service  # Initialize with a user service for user-related operations

    # Method to create a new appointment
    def create_appointment(self):
        users = db_list_users()  # Fetch users directly from the database
        if not users:
            print("No users found.")
            return

        # List all users
        for user in users:
            print(f"ID: {user['user_id']}, Name: {user['name']}, Timezone: {user['timezone']}")

        # Ask for user name
        user_name = input("Enter user name: ").strip()
        user = next((u for u in users if u['name'].lower() == user_name.lower()), None)

        if not user:
            print("User not found.")
            return

        print("Available Consultants:")  # Display list of available consultants
        for idx, consultant in enumerate(consultants, 1):  # Enumerate consultants with indices starting from 1
            print(f"{idx}. {consultant}")  # Print consultant details

        try:
            consultant_idx = int(input("Choose consultant: ")) - 1  # Get consultant choice and convert to zero-based index
            if consultant_idx not in range(len(consultants)):  # Validate consultant index
                raise ValueError("Invalid consultant index.")  # Raise error if index is invalid
            consultant = consultants[consultant_idx]  # Get selected consultant
        except ValueError as e:  # Handle invalid input
            print(e)  # Print error message
            return  # Exit the function

        print("Available slots:")  # Display available slots for the selected consultant
        slots = available_slots.get(consultant, [])  # Retrieve available slots for the consultant
        if not slots:  # Check if no slots are available
            print(f"No slots available for {consultant}.")  # Notify no slots available
            return  # Exit the function

        for idx, slot in enumerate(slots, 1):  # Enumerate slots with indices starting from 1
            print(f"{idx}. {slot}")  # Print slot details

        try:
            slot_idx = int(input("Choose a slot: ")) - 1  # Get slot choice and convert to zero-based index
            if slot_idx not in range(len(slots)):  # Validate slot index
                raise ValueError("Invalid slot index.")  # Raise error if index is invalid
            chosen_slot = slots.pop(slot_idx)  # Remove chosen slot from availability
        except ValueError as e:  # Handle invalid input
            print(e)  # Print error message
            return  # Exit the function

        customer_time = convert_to_timezone(chosen_slot, "UTC", user['timezone'])  # Convert slot to customer's timezone
        mentor_time = convert_to_timezone(chosen_slot, "UTC", "Europe/Bucharest")  # Convert slot to mentor's timezone

        appointment = Appointment(user, consultant, customer_time, mentor_time)  # Create appointment object with both times
        appointments.append(appointment)  # Add appointment to the list

        print("Appointment created successfully.")  # Confirm successful creation
        print(f"Appointment time in your timezone: {customer_time}")  # Display customer's timezone appointment
        print(f"Appointment time in Bucharest timezone: {mentor_time}")  # Display mentor's timezone appointment

    # Method to list all scheduled appointments
    def list_appointments(self):
        if not appointments:  # Check if there are no appointments
            print("No appointments scheduled.")  # Notify no appointments found
            return  # Exit the function

        for appt in appointments:  # Iterate through the list of appointments
            print(f"User: {appt.user['name']}, Consultant: {appt.consultant}")  # Print user and consultant details
            print(f"  Time in Customer's Timezone: {appt.customer_time}")  # Print appointment time in customer's timezone
            print(f"  Time in Mentor's Timezone (Bucharest): {appt.mentor_time}")  # Print appointment time in mentor's timezone
            print("-" * 40)  # Print separator for readability
