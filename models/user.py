class User:
    def _init_(self, user_id, name, timezone):
        self.user_id = user_id
        self.name = name
        self.timezone = timezone

    def _repr_(self):
        return f"User({self.user_id}, {self.name}, {self.timezone})"