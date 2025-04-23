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

    def _validate_duration(self, duration):
        if isinstance(duration, str):
            duration = int(duration)

        if duration <= 0:
            raise WorkOutDurationError()
        # Maximum minutes in a week (7*24*60), pretty hardcode goal
        if duration > 10080:
            raise WorkOutDurationError()
        
        return duration

    def get_all_user_workouts(self, username):
        workouts = self.workout_repository.find_all_by_username(username)
        return workouts
    
    def get_workout_by_id(self, workout_id):
        workout = self.workout_repository.find_one_by_id(workout_id)
        return workout

    def create_workout(self, username, type, duration):
        try:
            duration = self._validate_duration(duration)

            created_workout = self.workout_repository.create(
                Workout(username, type, duration, datetime.now()))
            return created_workout
           
        except ValueError:
            raise WorkOutDurationError("Please enter a valid number for workout duration.")
        
    def update_workout(self, workout):
        duration = workout.duration
        try:
            duration = self._validate_duration(duration)

            updated_workout = self.workout_repository.update(workout)
            return updated_workout
           
        except ValueError:
            raise WorkOutDurationError("Please enter a valid number for workout duration.")

    def get_weeks_workout_total(self, username):
        workout_total = self.workout_repository.get_current_weeks_workout_total(
            username)
        return workout_total


workout_service = WorkoutService()
