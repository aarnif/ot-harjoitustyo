import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_matti = User("matti", "password", 600)
        self.user_maija = User("maija", "password")

    def test_create_user(self):
        user_repository.create(self.user_matti)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "matti")
        self.assertEqual(users[0].password, "password")
        self.assertEqual(users[0].weekly_training_goal_in_minutes, 600)

    def test_default_weekly_training_goal_value(self):
        user_repository.create(self.user_maija)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "maija")
        self.assertEqual(users[0].password, "password")
        self.assertEqual(users[0].weekly_training_goal_in_minutes, 0)

    def test_find_by_username(self):
        user_repository.create(self.user_matti)
        user_repository.create(self.user_maija)
        user = user_repository.find_by_username(self.user_maija.username)
        self.assertEqual(user.username, "maija")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.weekly_training_goal_in_minutes, 0)

    def test_update_workout_goal(self):
        user_repository.create(self.user_maija)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "maija")
        self.assertEqual(users[0].password, "password")
        self.assertEqual(users[0].weekly_training_goal_in_minutes, 0)
        user_repository.update_weekly_training_goal(self.user_maija.username, 400)
        users = user_repository.find_all()
        self.assertEqual(users[0].weekly_training_goal_in_minutes, 400)

    
