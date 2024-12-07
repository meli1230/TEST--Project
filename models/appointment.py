class Appointment:
    def _init_(self, user, consultant, datetime):
        self.user = user
        self.consultant = consultant
        self.datetime = datetime

    def _repr_(self):
        return f"Appointment(User: {self.user.name}, Consultant: {self.consultant}, Time: {self.datetime})"