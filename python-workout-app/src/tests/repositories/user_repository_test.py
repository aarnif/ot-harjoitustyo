import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_matti = User('matti', 'password', 600)

    def test_create_user(self):
        user_repository.create(self.user_matti)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, 'matti')
        self.assertEqual(users[0].password, 'password')
        self.assertEqual(users[0].weekly_training_goal_in_minutes, 600)
