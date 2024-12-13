#from required modules and classes
from data.storage import appointments, consultants, users  #import data lists for appointments, consultants, and users
from models.appointment import Appointment  #import the Appointment model
from utils.timezone import convert_to_timezone  #import a utility function for timezone conversion

#service class to handle appointment-related functionality
class AppointmentService:
    #constructor for the AppointmentService class
    def __init__(self, user_service):
        self.user_service = user_service  #initialize with a user service for user-related operations

    #method to create a new appointment
    def create_appointment(self):
        self.user_service.list_users()  #list all available users using the user service

        user_name = input("Enter user name: ")  #prompt the user to input the name of the user for the appointment

        user = next((u for u in users if u.name.lower() == user_name.lower()), None)  #find the user by matching the input name (case insensitive)

        if not user:  #check if the user is not found
            print("User not found.")  #print an error message and exit the function
            return

        print("Available Consultants:")  #display a list of available consultants
        for idx, consultant in enumerate(consultants, 1):  #enumerate to display consultants with indices starting at 1
            print(f"{idx}. {consultant}")  #print consultant details

        consultant_idx = int(input("Choose consultant: ")) - 1  #prompt the user to choose a consultant and convert input to zero-based index

        if consultant_idx not in range(len(consultants)):  #check if the chosen consultant index is valid
            print("Invalid choice.")  #print an error message and exit
            return

        consultant = consultants[consultant_idx]  #get the selected consultant from the list

        datetime = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")  #prompt the user to input the appointment date and time

        local_time = convert_to_timezone(datetime, user.timezone)  #convert the input date and time to the user's timezone

        appointment = Appointment(user, consultant, local_time)  #create a new appointment using the Appointment model

        appointments.append(appointment)  #add the created appointment to the list of appointments

        print("Appointment created successfully.")  #confirm the successful creation of the appointment

    #method to list all scheduled appointments
    def list_appointments(self):
        if not appointments:  #check if there are no appointments
            print("No appointments scheduled.")  #print a message and exit the function
            return

        for appt in appointments:  #iterate through the list of appointments
            print(appt)  #print each appointment
