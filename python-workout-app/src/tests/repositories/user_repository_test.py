import unittest

from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_matti = User("matti", "password", 600)
        self.user_maija = User("maija", "password")

    def check_user_equality(self, user1, user2):
        self.assertEqual(user1.username, user2.username)
        self.assertEqual(user1.password, user2.password)
        self.assertEqual(user1.weekly_training_goal_in_minutes, user2.weekly_training_goal_in_minutes)

    def test_create_user(self):
        user_repository.create(self.user_matti)
        user = user_repository.find_by_username(self.user_matti.username)
        self.check_user_equality(user, self.user_matti)

    def test_default_weekly_training_goal_value(self):
        user_repository.create(self.user_maija)
        user = user_repository.find_by_username(self.user_maija.username)
        self.check_user_equality(user, self.user_maija)
        self.assertEqual(self.user_maija.weekly_training_goal_in_minutes, 0)

    def test_find_all_users(self):
        user_repository.create(self.user_matti)
        user_repository.create(self.user_maija)
        users = user_repository.find_all()
        self.assertEqual(len(users), 2)
        self.check_user_equality(users[0], self.user_matti)
        self.check_user_equality(users[1], self.user_maija)

    def test_find_by_username(self):
        user_repository.create(self.user_matti)
        user_repository.create(self.user_maija)
        user = user_repository.find_by_username(self.user_maija.username)
        self.check_user_equality(user, self.user_maija)

    def test_update_workout_goal(self):
        user_repository.create(self.user_maija)
        user = user_repository.find_by_username(self.user_maija.username)
        self.check_user_equality(user, self.user_maija)
        user_repository.update_weekly_training_goal(self.user_maija.username, 400)
        user = user_repository.find_by_username(self.user_maija.username)
        self.assertEqual(user.weekly_training_goal_in_minutes, 400)

    
