from datetime import datetime

from entities.workout import Workout
from repositories.workout_repository import (
    workout_repository as default_workout_repository
)


class WorkoutService:
    def __init__(self, workout_repository=default_workout_repository):
        self.workout_repository = workout_repository

    def get_all_user_workouts(self, username):
        workouts = self.workout_repository.find_all_by_username(username)
        return workouts

    def create_workout(self, username, type, duration):
        created_at = datetime.now()
        workout = self.workout_repository.create(Workout(username, type, duration, created_at))

        return workout
    
    def get_weeks_workout_total(self, username):
        workout_total = self.workout_repository.get_current_weeks_workout_total(username)
        return workout_total


workout_service = WorkoutService()
