from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT username, password, weekly_training_goal_in_minutes FROM users")

        rows = cursor.fetchall()

        users = [User(row["username"], row["password"], row["weekly_training_goal_in_minutes"]) for row in rows]

        return users
    
    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT username, password, weekly_training_goal_in_minutes FROM users  WHERE username = ?", (username,))

        row = cursor.fetchone()

        user = User(row["username"], row["password"], row["weekly_training_goal_in_minutes"])

        return user
    
    def create(self, user):
        cursor = self._connection.cursor()
        
        cursor.execute(
            "INSERT INTO users (username, password, weekly_training_goal_in_minutes) VALUES (?, ?, ?)",
            (user.username, user.password, user.weekly_training_goal_in_minutes)
        )
        
        self._connection.commit()
        
        return user


user_repository = UserRepository(get_database_connection())

if __name__ == "__main__":
    user_repository.create(User("test", "password", 600))