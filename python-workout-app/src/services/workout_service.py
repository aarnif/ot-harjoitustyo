from datetime import datetime

from entities.workout import Workout
from repositories.workout_repository import (
    workout_repository as default_workout_repository
)

class WorkOutDurationError(Exception):
    def __init__(self, message="Workout duration must be number between 1 and 10080."):
        self.message = message
        super().__init__(self.message)


class WorkoutService:
    def __init__(self, workout_repository=default_workout_repository):
        self.workout_repository = workout_repository

    def get_all_user_workouts(self, username):
        workouts = self.workout_repository.find_all_by_username(username)
        return workouts

    def create_workout(self, username, type, duration):
        try:
            if isinstance(duration, str):
                duration = int(duration)

            if duration <= 0:
                raise WorkOutDurationError()
            # Maximum minutes in a week (7*24*60), pretty hardcode goal
            if duration > 10080:
                raise WorkOutDurationError()

            created_workout = self.workout_repository.create(
                Workout(username, type, duration, datetime.now()))
            return created_workout
           
        except ValueError:
            raise WorkOutDurationError("Please enter a valid number for workout duration.")

    def get_weeks_workout_total(self, username):
        workout_total = self.workout_repository.get_current_weeks_workout_total(
            username)
        return workout_total


workout_service = WorkoutService()
