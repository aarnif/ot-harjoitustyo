class User:
    def __init__(self, username, password, weekly_training_goal_in_minutes=0):
        self.username = username
        self.password = password
        self.weekly_training_goal_in_minutes = weekly_training_goal_in_minutes
