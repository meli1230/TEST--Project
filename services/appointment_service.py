from Database.database import appointments_table
from data.storage import appointments, consultants, available_slots, users  #import data lists for appointments, consultants, and users
from models.appointment import Appointment  #import the Appointment model
from utils.timezone import convert_to_timezone  #import a utility function for timezone conversion

#service class to handle appointment-related functionality
class AppointmentService:
    #constructor for the AppointmentService class
    def __init__(self, appointments_table, user_service):
        self.appointments_table = appointments_table  # Store the appointments table
        self.user_service = user_service  #initialize with a user service for user-related operations

    #method to create a new appointment
    def create_appointment(self):
        self.user_service.list_users()  #list all available users
        user_name = input("Enter user name: ").strip()  #prompt user for their name and remove extra spaces
        user = next((u for u in users if u.name.lower() == user_name.lower()), None)  #find user by name, case insensitive

        if not user:  #check if user is not found
            print("User not found.")  #notify user not found
            return  #exit the function

        print("Available Consultants:")  #display list of available consultants
        for idx, consultant in enumerate(consultants, 1):  #enumerate consultants with indices starting from 1
            print(f"{idx}. {consultant}")  #print consultant details

        try:
            consultant_idx = int(input("Choose consultant: ")) - 1  #get consultant choice and convert to zero-based index
            if consultant_idx not in range(len(consultants)):  #validate consultant index
                raise ValueError("Invalid consultant index.")  #raise error if index is invalid
            consultant = consultants[consultant_idx]  #get selected consultant
        except ValueError as e:  #handle invalid input
            print(e)  #print error message
            return  #exit the function

        print("Available slots:")  #display available slots for the selected consultant
        slots = available_slots.get(consultant, [])  #retrieve available slots for the consultant
        if not slots:  #check if no slots are available
            print(f"No slots available for {consultant}.")  #notify no slots available
            return  #exit the function

        for idx, slot in enumerate(slots, 1):  #enumerate slots with indices starting from 1
            print(f"{idx}. {slot}")  #print slot details

        try:
            slot_idx = int(input("Choose a slot: ")) - 1  #get slot choice and convert to zero-based index
            if slot_idx not in range(len(slots)):  #validate slot index
                raise ValueError("Invalid slot index.")  #raise error if index is invalid
            chosen_slot = slots.pop(slot_idx)  #remove chosen slot from availability
        except ValueError as e:  #handle invalid input
            print(e)  #print error message
            return  #exit the function

        customer_time = convert_to_timezone(chosen_slot, "UTC", user.timezone)  #convert slot to customer's timezone
        mentor_time = convert_to_timezone(chosen_slot, "UTC", "Europe/Bucharest")  #convert slot to mentor's timezone

        appointment = Appointment(user, consultant, customer_time, mentor_time)  #create appointment object with both times
        appointments.append(appointment)  #add appointment to the list

        print("Appointment created successfully.")  #confirm successful creation
        print(f"Appointment time in your timezone: {customer_time}")  #display customer's timezone appointment
        print(f"Appointment time in Bucharest timezone: {mentor_time}")  #display mentor's timezone appointment

    #method to list all scheduled appointments
    def list_appointments(self):
        if not appointments:  #check if there are no appointments
            print("No appointments scheduled.")  #notify no appointments found
            return  #exit the function

        for appt in appointments:  #iterate through the list of appointments
            print(f"User: {appt.user.name}, Consultant: {appt.consultant}")  #print user and consultant details
            print(f"  Time in Customer's Timezone: {appt.customer_time}")  #print appointment time in customer's timezone
            print(f"  Time in Mentor's Timezone (Bucharest): {appt.mentor_time}")  #print appointment time in mentor's timezone
            print("-" * 40)  #print separator for readability
