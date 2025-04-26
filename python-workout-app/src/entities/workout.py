class Workout:
    def __init__(self, username, workout_type, workout_duration, created_at, workout_id=None):
        self.id = workout_id
        self.username = username
        self.type = workout_type
        self.duration = workout_duration
        self.created_at = created_at
