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


class InvalidCredentialsError(Exception):
    def __init__(self, message="Invalid username or password. Please try again."):
        self.message = message
        super().__init__(self.message)


class WorkoutGoalError(Exception):
    def __init__(self, message="Workout goal must be number between 0 and 10080."):
        self.message = message
        super().__init__(self.message)
# generoitu koodi päättyy


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._current_user = None
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

        self._current_user = user

        return user

    def update_workout_goal(self, new_goal):
        # generoitu koodi alkaa
        try:
            if isinstance(new_goal, str):
                new_goal = int(new_goal)

            if new_goal < 0:
                raise WorkoutGoalError()
            # Maximum minutes in a week (7*24*60), pretty hardcode goal
            if new_goal > 10080:
                raise WorkoutGoalError()

            updated_user = self.user_repository.update_weekly_training_goal(
                self._current_user.username, new_goal)
            self._current_user = updated_user

        except ValueError:
            raise WorkoutGoalError(
                "Please enter a valid number for workout goal.")
        # generoitu koodi päättyy

    def login_user(self, username, password):
        existing_user = self.user_repository.find_by_username(
            username)

        if not existing_user or existing_user.password != password:
            raise InvalidCredentialsError()

        self._current_user = existing_user

        return existing_user

    def current_user(self):
        return self._current_user

    def logout_user(self):
        self._current_user = None


user_service = UserService()
