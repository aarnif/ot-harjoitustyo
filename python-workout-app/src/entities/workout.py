class Workout:
    def __init__(self, username, type, duration, created_at, id=None):
        self.id = id
        self.username = username
        self.type = type
        self.duration = duration
        self.created_at = created_at
