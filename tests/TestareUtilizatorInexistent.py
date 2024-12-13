import unittest
from unittest.mock import MagicMock
from services.user_service import UserService
from services.appointment_service import AppointmentService

class TestareAppointmentUtilizatorInexistent(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.appointment_service = AppointmentService(self.user_service)

        self.user_service.list_users = MagicMock(return_value=["John Doe", "Jane Smith"])
        self.appointment_service.list_appointments_by_user = MagicMock(return_value=[])

    def test_list_appointments_for_nonexistent_user(self):
        nonexistent_user = "Alex Johnson"
        appointments = self.appointment_service.list_appointments_by_user(nonexistent_user)

        self.appointment_service.list_appointments_by_user.assert_called_once_with(nonexistent_user)
        self.assertEqual(len(appointments), 0)


