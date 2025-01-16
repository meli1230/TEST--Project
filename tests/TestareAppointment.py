#import required modules and classes for testing
import unittest  #import the unittest module for unit testing
from unittest.mock import MagicMock  #import MagicMock for mocking methods
from services.user_service import UserService  #import the UserService class
from services.appointment_service import AppointmentService  #import the AppointmentService class

#test class for appointment-related functionality
class TestareAppointment(unittest.TestCase):
    def setUp(self):  #setup method to initialize test dependencies
        self.user_service = UserService()  #create an instance of UserService
        self.appointment_service = AppointmentService(self.user_service)  #create an instance of AppointmentService with user_service

        self.appointment_service.list_appointments = MagicMock(return_value=[  #mock the list_appointments method
            {"user": "John Doe", "date": "2024-12-12 10:00"},  #mocked appointment for John Doe
            {"user": "Jane Smith", "date": "2024-12-13 15:00"}  #mocked appointment for Jane Smith
        ])
        self.appointment_service.create_appointment = MagicMock()  #mock the create_appointment method

    def test_create_appointment(self):  #test method for creating an appointment
        self.appointment_service.create_appointment("Jane Smith", "2024-12-15 14:00")  #call the mocked create_appointment method
        self.appointment_service.create_appointment.assert_called_once_with("Jane Smith", "2024-12-15 14:00")  #verify it was called with the correct arguments

    def test_list_appointments(self):  #test method for listing appointments
        appointments = self.appointment_service.list_appointments()  #call the mocked list_appointments method
        self.appointment_service.list_appointments.assert_called_once()  #verify the method was called exactly once
        self.assertEqual(len(appointments), 2)  #assert that the list contains two appointments
        self.assertEqual(appointments[0]["user"], "John Doe")  #assert that the first appointment is for John Doe

if __name__ == "__main__":  #run the tests if the script is executed directly
    unittest.main()  #run all the test cases
