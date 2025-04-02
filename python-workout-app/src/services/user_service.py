from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

# generoitu koodi alkaa


class UserNameLengthError(Exception):
    def __init__(self, message="Username must be at least 3 characters long."):
        self.message = message
        super().__init__(self.message)


class PasswordLengthError(Exception):
    def __init__(self, message="Password must be at least 6 characters long."):
        self.message = message
        super().__init__(self.message)


class PasswordMatchError(Exception):
    def __init__(self, message="Passwords do not match."):
        self.message = message
        super().__init__(self.message)


class UserNameExistsError(Exception):
    def __init__(self, message="User with the same username already exists."):
        self.message = message
        super().__init__(self.message)
# generoitu koodi päättyy


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self.user_repository = user_repository

    def create_user(self, username, password, confirm_password):

        if len(username) < 3:
            raise UserNameLengthError()

        if len(password) < 6:
            raise PasswordLengthError()

        if password != confirm_password:
            raise PasswordMatchError()

        check_if_user_already_exist = self.user_repository.find_by_username(
            username)

        if check_if_user_already_exist:
            raise UserNameExistsError()

        user = self.user_repository.create(User(username, password))

        return user


user_service = UserService()
