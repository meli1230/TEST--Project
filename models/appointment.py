class Appointment:
    def __init__(self, user, consultant, datetime):
        self.user = user
        self.consultant = consultant
        self.datetime = datetime

    def __repr__(self):
        return f"Appointment(User: {self.user.name}, Consultant: {self.consultant}, Time: {self.datetime})"
