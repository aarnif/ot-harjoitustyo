from entities.user import User
from database_connection import get_database_connection


def get_user_from_row(row):
    if row:
        return User(row["username"], row["password"], row["weekly_training_goal_in_minutes"])

    return None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT username, password, weekly_training_goal_in_minutes FROM users")

        rows = cursor.fetchall()

        users = [get_user_from_row(row) for row in rows]

        return users

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT username, password, "
                       "weekly_training_goal_in_minutes FROM users WHERE username = ?",
                       (username,))

        row = cursor.fetchone()

        user = get_user_from_row(row)

        return user

    def create(self, user):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO users (username, password, weekly_training_goal_in_minutes) "
            "VALUES (?, ?, ?)",
            (user.username, user.password, user.weekly_training_goal_in_minutes)
        )

        self._connection.commit()

        return user

    def update_weekly_training_goal(self, username, new_weekly_training_goal):
        cursor = self._connection.cursor()

        cursor.execute("UPDATE users SET weekly_training_goal_in_minutes = ? WHERE username = ?",
                       (new_weekly_training_goal, username))

        self._connection.commit()


user_repository = UserRepository(get_database_connection())

if __name__ == "__main__":
    user_repository.create(User("test", "password", 600))
