from datetime import datetime, timedelta

from entities.workout import Workout
from database_connection import get_database_connection


def get_workout_from_row(row):
    if row:
        return Workout(row["username"], row["type"], row["duration"], row["created_at"], row["id"])

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
            "SELECT id, username, type, duration, created_at FROM workouts WHERE username = ?",
            (username,))

        rows = cursor.fetchall()

        workouts = [get_workout_from_row(row) for row in rows]

        return workouts

    def find_one_by_id(self, id):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, username, type, duration, created_at FROM workouts WHERE id = ?",
            (id,))

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

        # generoitu koodi alkaa
        workout.id = cursor.lastrowid
        # generoitu koodi päättyy

        return workout
    
    # generoitu koodi alkaa
    def update(self, workout):
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE workouts "
            "SET type = ?, duration = ? "
            "WHERE id = ? AND username = ?",
            (workout.type, workout.duration, workout.id, workout.username)
        )
        self._connection.commit()
        return workout
    
    def delete(self, workout_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM workouts WHERE id = ?",
            (workout_id,)
        )
        self._connection.commit()
        return cursor.rowcount > 0
    
    def get_current_weeks_workout_total(self, username):
        workouts = self.find_all_by_username(username)

        if len(workouts) == 0:
            return 0

        today = datetime.now()

        start_of_week = today - timedelta(days=today.weekday())
        start_of_week = datetime(
            start_of_week.year, start_of_week.month, start_of_week.day)

        end_of_week = start_of_week + timedelta(days=6)
        end_of_week = datetime(
            end_of_week.year, end_of_week.month, end_of_week.day, 23, 59)

        current_week_workouts = []
        for workout in workouts:
            workout_date = datetime.strptime(
                workout.created_at, "%Y-%m-%d %H:%M:%S")
            if start_of_week <= workout_date <= end_of_week:
                current_week_workouts.append(workout)

        total_workout_time = sum(
            workout.duration for workout in current_week_workouts)

        return total_workout_time
    # generoitu koodi päättyy


workout_repository = WorkoutRepository(get_database_connection())
