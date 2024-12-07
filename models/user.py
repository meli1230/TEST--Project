class User:
    def __init__(self, user_id, name, timezone):
        self.user_id = user_id
        self.name = name
        self.timezone = timezone

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.timezone})"
