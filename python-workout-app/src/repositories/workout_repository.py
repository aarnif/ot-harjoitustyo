from entities.workout import Workout
from database_connection import get_database_connection


def get_workout_from_row(row):
    if row:
        return Workout(row["username"], row["type"], row["duration"], row["created_at"])

    return None


class WorkoutRepository:
    def __init__(self, connection):
        self._connection = connection

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM workouts")
        self._connection.commit()

    def find_all_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT username, type, duration, created_at FROM workouts WHERE username = ?",
                       (username,))

        rows = cursor.fetchall()

        workouts = [get_workout_from_row(row) for row in rows]

        return workouts
    
    def find_one_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT username, type, duration, created_at FROM workouts WHERE username = ?",
                       (username,))

        row = cursor.fetchone()

        workout = get_workout_from_row(row)

        return workout

    def create(self, workout):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO workouts (username, type, duration, created_at) "
            "VALUES (?, ?, ?, ?)",
            (workout.username, workout.type, workout.duration, workout.created_at)
        )

        self._connection.commit()

        return workout


workout_repository = WorkoutRepository(get_database_connection())
