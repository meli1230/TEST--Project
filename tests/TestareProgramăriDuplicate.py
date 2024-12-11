import unittest
from unittest.mock import MagicMock
from services.user_service import UserService
from services.appointment_service import AppointmentService

class TestareAppointmentDuplicat(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.appointment_service = AppointmentService(self.user_service)

        self.appointment_service.list_appointments = MagicMock(return_value=[
            {"user": "John Doe", "date": "2024-12-12 10:00"}
        ])
        self.appointment_service.create_appointment = MagicMock(side_effect=ValueError("Appointment already exists"))

    def test_duplicate_appointment(self):
        user = "John Doe"
        date = "2024-12-12 10:00"

        with self.assertRaises(ValueError) as context:
            self.appointment_service.create_appointment(user, date)

        self.appointment_service.create_appointment.assert_called_once_with(user, date)
        self.assertEqual(str(context.exception), "Appointment already exists")
