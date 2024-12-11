import unittest
from unittest.mock import MagicMock
from services.user_service import UserService
from services.appointment_service import AppointmentService


class TestareAppointment(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.appointment_service = AppointmentService(self.user_service)

        self.appointment_service.list_appointments = MagicMock(return_value=[
            {"user": "John Doe", "date": "2024-12-12 10:00"},
            {"user": "Jane Smith", "date": "2024-12-13 15:00"}
        ])
        self.appointment_service.create_appointment = MagicMock()

    def test_create_appointment(self):
        self.appointment_service.create_appointment("Jane Smith", "2024-12-15 14:00")
        self.appointment_service.create_appointment.assert_called_once_with("Jane Smith", "2024-12-15 14:00")

    def test_list_appointments(self):
        appointments = self.appointment_service.list_appointments()
        self.appointment_service.list_appointments.assert_called_once()
        self.assertEqual(len(appointments), 2)
        self.assertEqual(appointments[0]["user"], "John Doe")


if __name__ == "__main__":
    unittest.main()