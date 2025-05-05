from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

# generoitu koodi alkaa


class UserNameLengthError(Exception):
    """Poikkeus, joka heitetään, jos käyttäjätunnus on liian lyhyt.

    Args:
        message (str, optional): Virheilmoituksen viesti. 
        Oletusarvo "Username must be at least 3 characters long."
    """

    def __init__(self, message="Username must be at least 3 characters long."):
        self.message = message
        super().__init__(self.message)


class PasswordLengthError(Exception):
    """Poikkeus, joka heitetään, jos salasana on liian lyhyt.

    Args:
        message (str, optional): Virheilmoituksen viesti. 
        Oletusarvo "Password must be at least 6 characters long."
    """

    def __init__(self, message="Password must be at least 6 characters long."):
        self.message = message
        super().__init__(self.message)


class PasswordMatchError(Exception):
    """Poikkeus, joka heitetään, jos salasanat eivät täsmää.

    Args:
        message (str, optional): Virheilmoituksen viesti. Oletusarvo "Passwords do not match."
    """

    def __init__(self, message="Passwords do not match."):
        self.message = message
        super().__init__(self.message)


class UserNameExistsError(Exception):
    """Poikkeus, joka heitetään, jos käyttäjätunnus on jo olemassa.

    Args:
        message (str, optional): Virheilmoituksen viesti. 
        Oletusarvo "User with the same username already exists."
    """

    def __init__(self, message="User with the same username already exists."):
        self.message = message
        super().__init__(self.message)


class InvalidCredentialsError(Exception):
    """Poikkeus, joka heitetään, jos kirjautumistiedot ovat virheelliset.

    Args:
        message (str, optional): Virheilmoituksen viesti. 
        Oletusarvo "Invalid username or password. Please try again."
    """

    def __init__(self, message="Invalid username or password. Please try again."):
        self.message = message
        super().__init__(self.message)


class WorkoutGoalError(Exception):
    """Poikkeus, joka heitetään, jos treenitavoite on virheellinen.

    Args:
        message (str, optional): Virheilmoituksen viesti. 
        Oletusarvo "Workout goal must be number between 0 and 10080."
    """

    def __init__(self, message="Workout goal must be number between 0 and 10080."):
        self.message = message
        super().__init__(self.message)
# generoitu koodi päättyy


class UserService:
    """Käyttäjiin liittyvästä sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            user_repository (UserRepository, optional): Olio, joka omaa UserRepository-luokkaa 
            vastaavat metodit. Oletusarvo UserRepository-olio.
        """
        self._current_user = None
        self._user_repository = user_repository

    def create_user(self, username, password, confirm_password):
        """Luo uuden käyttäjän.

        Args:
            username (str): Käyttäjätunnus
            password (str): Salasana
            confirm_password (str): Salasanan vahvistus

        Raises:
            UserNameLengthError: Käyttäjätunnus on liian lyhyt
            PasswordLengthError: Salasana on liian lyhyt
            PasswordMatchError: Salasana ja sen vahvistus eivät täsmää
            UserNameExistsError: Käyttäjätunnus on jo olemassa

        Returns:
            User: Luotu uusi käyttäjä joka on User-olio
        """

        if len(username) < 3:
            raise UserNameLengthError()

        if len(password) < 6:
            raise PasswordLengthError()

        if password != confirm_password:
            raise PasswordMatchError()

        check_if_user_already_exist = self._user_repository.find_by_username(
            username)

        if check_if_user_already_exist:
            raise UserNameExistsError()

        user = self._user_repository.create(User(username, password))

        self._current_user = user

        return user

    def update_workout_goal(self, new_goal):
        """Päivittää käyttäjän viikoittaisen treenitavoitteen.

        Args:
            new_goal (int): Uusi viikottainen treenitavoite minuutteina

        Raises:
            WorkoutGoalError: Treenitavoite on negatiivinen luku
            WorkoutGoalError: Treenitavoite on liian suuri luku
            WorkoutGoalError: Treenitavoite ei ole luku
        """
        # generoitu koodi alkaa
        try:
            if isinstance(new_goal, str):
                new_goal = int(new_goal)

            if new_goal < 0:
                raise WorkoutGoalError()
            # Maximum minutes in a week (7*24*60)
            if new_goal > 10080:
                raise WorkoutGoalError()

            updated_user = self._user_repository.update_weekly_training_goal(
                self._current_user.username, new_goal)
            self._current_user = updated_user

        except ValueError as exc:
            raise WorkoutGoalError(
                "Please enter a valid number for workout goal.") from exc
        # generoitu koodi päättyy

    def login_user(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username (str): Käyttäjätunnus
            password (str): Salasana

        Raises:
            InvalidCredentialsError: Käyttäjätunnus tai salasana on virheellinen

        Returns:
            User: Kirjautunut käyttäjä joka on User-olio
        """
        existing_user = self._user_repository.find_by_username(
            username)

        if not existing_user or existing_user.password != password:
            raise InvalidCredentialsError()

        self._current_user = existing_user

        return existing_user

    def current_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            User | None: Kirjautunut käyttäjä joka on User-olio. 
            Palauttaa None, jos käyttäjä ei ole kirjautunut sisään.
        """
        return self._current_user

    def logout_user(self):
        """Kirjaa kirjautuneen käyttäjän ulos.
        """
        self._current_user = None


user_service = UserService()
