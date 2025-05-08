from entities.user import User
from database_connection import get_database_connection


def get_user_from_row(row):
    """Muodostaa User-olion tietokannan rivistä.

    Args:
        row (dict | None): Tietokannan rivi, joka sisältää käyttäjätiedot. 
        Voi olla None jos käyttäjää ei löydy.

    Returns:
        User | None: User-olio, joka vastaa tietokannan riviä, tai None jos riviä ei löydy.
    """
    if row:
        return User(row["username"], row["password"], row["weekly_training_goal_in_minutes"])

    return None


class UserRepository:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantatoiminnoista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection (sqlite3.Connection): Tietokantayhteys
        """
        self._connection = connection

    # generoitu koodi alkaa
    def _execute_query(self, query, params=None):
        cursor = self._connection.cursor()
        cursor.execute(query, params or ())
        return cursor
    # generoitu koodi päätty

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta.
        """
        self._execute_query("DELETE FROM users")
        self._connection.commit()

    def find_all(self):
        """Hakee kaikki käyttäjät tietokannasta.

        Returns:
            list[User]: Lista kaikista User-olioista
        """
        cursor = self._execute_query(
            "SELECT username, password, weekly_training_goal_in_minutes FROM users")

        rows = cursor.fetchall()
        users = [get_user_from_row(row) for row in rows]

        return users

    def find_by_username(self, username):
        """Hakee käyttäjän tietokannasta käyttäjätunnuksen perusteella.

        Args:
            username (str): Käyttäjätunnus

        Returns:
            User: User-olio, joka vastaa annettua käyttäjätunnusta
        """
        cursor = self._execute_query(
            "SELECT username, password, \
            weekly_training_goal_in_minutes FROM users WHERE username = ?",
            (username,))

        row = cursor.fetchone()
        return get_user_from_row(row)

    def create(self, user):
        """Luo uuden käyttäjän tietokantaan.

        Args:
            user (User): User-olio, joka halutaan luoda

        Returns:
            User: Luotu User-olio
        """
        self._execute_query(
            "INSERT INTO users (username, password, \
            weekly_training_goal_in_minutes) VALUES (?, ?, ?)",
            (user.username, user.password, user.weekly_training_goal_in_minutes)
        )

        self._connection.commit()
        return user

    def update_weekly_training_goal(self, username, new_weekly_training_goal):
        """Päivittää käyttäjän viikoittaisen treenitavoitteen tietokannassa.

        Args:
            username (str): Käyttäjätunnus
            new_weekly_training_goal (int): Uusi viikoittainen treenitavoite minuutteina

        Returns:
            User: Päivitetty User-olio
        """
        self._execute_query(
            "UPDATE users SET weekly_training_goal_in_minutes = ? WHERE username = ?",
            (new_weekly_training_goal, username)
        )

        self._connection.commit()
        updated_user = self.find_by_username(username)

        return updated_user


user_repository = UserRepository(get_database_connection())
