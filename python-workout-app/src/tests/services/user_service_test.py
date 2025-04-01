import unittest
import pytest

from repositories.user_repository import user_repository
from entities.user import User
from services.user_service import user_service, UserNameLengthError, PasswordLengthError, UserNameExistsError

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_matti = User("matti", "password", 600)
        self.username_too_short = UserNameLengthError()
        self.password_too_short = PasswordLengthError()
        self.user_exists_error = UserNameExistsError()

    def check_user_equality(self, user1, user2):
        self.assertEqual(user1.username, user2.username)
        self.assertEqual(user1.password, user2.password)
        self.assertEqual(user1.weekly_training_goal_in_minutes, user2.weekly_training_goal_in_minutes)

    def test_create_user(self):
        user = user_service.create_user(self.user_matti.username, 
                                        self.user_matti.password, 
                                        self.user_matti.weekly_training_goal_in_minutes)
        self.check_user_equality(user, self.user_matti)

    def test_username_too_short(self):
        too_short_username = "ma"
        with pytest.raises(UserNameLengthError) as error:
            user_service.create_user(too_short_username, 
                                            self.user_matti.password, 
                                            self.user_matti.weekly_training_goal_in_minutes)
        self.assertEqual(str(error.value), self.username_too_short.message)

    def test_password_too_short(self):
        too_short_password = "pass"
        with pytest.raises(PasswordLengthError) as error:
            user_service.create_user(self.user_matti.username, 
                                            too_short_password, 
                                            self.user_matti.weekly_training_goal_in_minutes)
        self.assertEqual(str(error.value), self.password_too_short.message)

    def test_try_to_create_user_with_same_username(self):
        user = user_service.create_user(self.user_matti.username, 
                                        self.user_matti.password, 
                                        self.user_matti.weekly_training_goal_in_minutes)
        self.check_user_equality(user, self.user_matti)
        with pytest.raises(UserNameExistsError) as error:
            user_service.create_user(self.user_matti.username, 
                                            self.user_matti.password, 
                                            self.user_matti.weekly_training_goal_in_minutes)
        self.assertEqual(str(error.value), self.user_exists_error.message)


    
