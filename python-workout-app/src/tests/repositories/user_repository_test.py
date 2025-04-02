import unittest

from tests.test_helpers import TestHelpers
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.test_helpers = TestHelpers()
        user_repository.delete_all()
        self.user_matti = User("matti", "password", 600)
        self.user_maija = User("maija", "password")

    def test_create_user(self):
        user_repository.create(self.user_matti)
        user = user_repository.find_by_username(self.user_matti.username)
        self.test_helpers.check_user_equality(user, self.user_matti)

    def test_default_weekly_training_goal_value(self):
        user_repository.create(self.user_maija)
        user = user_repository.find_by_username(self.user_maija.username)
        self.test_helpers.check_user_equality(user, self.user_maija)
        self.assertEqual(self.user_maija.weekly_training_goal_in_minutes, 0)

    def test_find_all_users(self):
        user_repository.create(self.user_matti)
        user_repository.create(self.user_maija)
        users = user_repository.find_all()
        self.assertEqual(len(users), 2)
        self.test_helpers.check_user_equality(users[0], self.user_matti)
        self.test_helpers.check_user_equality(users[1], self.user_maija)

    def test_find_by_username(self):
        user_repository.create(self.user_matti)
        user_repository.create(self.user_maija)
        user = user_repository.find_by_username(self.user_maija.username)
        self.test_helpers.check_user_equality(user, self.user_maija)

    def test_update_workout_goal(self):
        user_repository.create(self.user_maija)
        user = user_repository.find_by_username(self.user_maija.username)
        self.test_helpers.check_user_equality(user, self.user_maija)
        user_repository.update_weekly_training_goal(
            self.user_maija.username, 400)
        user = user_repository.find_by_username(self.user_maija.username)
        self.assertEqual(user.weekly_training_goal_in_minutes, 400)
