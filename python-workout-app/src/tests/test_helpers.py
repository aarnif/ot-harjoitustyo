import unittest


class TestHelpers(unittest.TestCase):
    def check_user_equality(self, user1, user2):
        self.assertEqual(user1.username, user2.username)
        self.assertEqual(user1.password, user2.password)
        self.assertEqual(user1.weekly_training_goal_in_minutes,
                         user2.weekly_training_goal_in_minutes)
        
    def check_workout_equality(self, workout1, workout2):
        self.assertEqual(workout1.username, workout2.username)
        self.assertEqual(workout1.type, workout2.type)
        self.assertEqual(workout1.duration,
                         workout2.duration)
