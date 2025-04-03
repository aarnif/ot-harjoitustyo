import unittest
import pytest

from tests.test_helpers import TestHelpers
from repositories.user_repository import user_repository
from entities.user import User
from services.user_service import user_service, UserNameLengthError, PasswordLengthError, PasswordMatchError, UserNameExistsError, InvalidCredentialsError


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.test_helpers = TestHelpers()
        user_repository.delete_all()
        self.user_matti = User("matti", "password")
        self.username_too_short = UserNameLengthError()
        self.password_too_short = PasswordLengthError()
        self.password_do_not_match = PasswordMatchError()
        self.user_exists_error = UserNameExistsError()
        self.invalid_credentials_error = InvalidCredentialsError()

    def test_create_user(self):
        user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        self.test_helpers.check_user_equality(user, self.user_matti)

    def test_username_too_short(self):
        too_short_username = "ma"
        with pytest.raises(UserNameLengthError) as error:
            user_service.create_user(too_short_username,
                                     self.user_matti.password,
                                     self.user_matti.password)
        self.assertEqual(str(error.value), self.username_too_short.message)

    def test_password_too_short(self):
        too_short_password = "pass"
        with pytest.raises(PasswordLengthError) as error:
            user_service.create_user(self.user_matti.username,
                                     too_short_password,
                                     too_short_password)
        self.assertEqual(str(error.value), self.password_too_short.message)

    def test_passwords_do_not_match(self):
        wrong_confirm_password = "passwor"
        with pytest.raises(PasswordMatchError) as error:
            user_service.create_user(self.user_matti.username,
                                     self.user_matti.password,
                                     wrong_confirm_password,)
        self.assertEqual(str(error.value), self.password_do_not_match.message)

    def test_try_to_create_user_with_same_username(self):
        user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        self.test_helpers.check_user_equality(user, self.user_matti)
        with pytest.raises(UserNameExistsError) as error:
            user_service.create_user(self.user_matti.username,
                                     self.user_matti.password,
                                     self.user_matti.password)
        self.assertEqual(str(error.value), self.user_exists_error.message)

    def test_login_user(self):
        new_user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        logged_in_user = user_service.login_user(new_user.username,
                                        new_user.password)
        self.test_helpers.check_user_equality(logged_in_user, self.user_matti)

    def test_login_fails_with_wrong_username(self):
        new_user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        wrong_username = new_user.username[:-1]
        with pytest.raises(InvalidCredentialsError) as error:
            user_service.login_user(wrong_username, new_user.password)
        self.assertEqual(str(error.value), self.invalid_credentials_error.message)

    def test_login_fails_with_wrong_password(self):
        new_user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        wrong_password = new_user.password[:-1]
        with pytest.raises(InvalidCredentialsError) as error:
            user_service.login_user(new_user.username, wrong_password)
        self.assertEqual(str(error.value), self.invalid_credentials_error.message)

    def test_user_stays_logged_in(self):
        user_service.create_user(self.user_matti.username,
                                self.user_matti.password,
                                self.user_matti.password)
        user_service.login_user(self.user_matti.username, self.user_matti.password)
        current_user = user_service.current_user()
        self.test_helpers.check_user_equality(current_user, self.user_matti)

    def logout_works(self):
        user_service.create_user(self.user_matti.username,
                                self.user_matti.password,
                                self.user_matti.password)
        user_service.login_user(self.user_matti.username, self.user_matti.password)
        user_service.logout_user()
        current_user = user_service.current_user()
        self.test_helpers.check_user_equality(current_user, None)

        
