#class for appointments
class Appointment:
    def __init__(self, user, consultant, datetime):
        '''
        Initializes an appointment object with the following parameters:
        :param user: the user who booked the appointment
        :param consultant: the consultant assigned for this appointment
        :param datetime: the date and time of the appointment
        '''
        self.user = user
        self.consultant = consultant
        self.datetime = datetime

    def __repr__(self):
        '''
        Defines a string representation of the appointment object
        :return: user name, consultant, time
        '''
        return f"Appointment(User: {self.user.name}, Consultant: {self.consultant}, Time: {self.datetime})"

