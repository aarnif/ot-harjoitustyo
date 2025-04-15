from datetime import datetime

import unittest
import pytest

from tests.test_helpers import TestHelpers
from repositories.user_repository import user_repository
from repositories.workout_repository import workout_repository
from entities.user import User
from entities.workout import Workout
from services.workout_service import workout_service
from services.user_service import user_service


class TestWorkoutService(unittest.TestCase):
    def setUp(self):
        self.test_helpers = TestHelpers()
        workout_repository.delete_all()
        user_repository.delete_all()
        self.user_matti = User("matti", "password")
        self.workout = Workout("matti", "cardio", 60, datetime.now())

    def test_get_all_workouts(self):
        user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        workouts = workout_service.get_all_user_workouts(user.username)
        self.assertEqual(workouts, [])
        workout_service.create_workout(self.user_matti.username,
                                       self.workout.type,
                                       self.workout.duration)
        workouts = workout_service.get_all_user_workouts(user.username)
        self.assertEqual(len(workouts), 1)

    def test_create_workout(self):
        user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        workout = workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 self.workout.duration)
        self.test_helpers.check_workout_equality(workout, self.workout)
        self.assertEqual(workout.username, user.username)

    def test_get_weeks_workout_total(self):
        user_service.create_user(self.user_matti.username,
                                 self.user_matti.password,
                                 self.user_matti.password)

        number_of_added_workouts = 3

        for _ in range(number_of_added_workouts):
            workout_service.create_workout(self.user_matti.username,
                                           self.workout.type,
                                           self.workout.duration)

        workout_total = workout_service.get_weeks_workout_total(
            self.user_matti.username)
        self.assertEqual(workout_total, self.workout.duration *
                         number_of_added_workouts)
