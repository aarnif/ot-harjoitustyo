from datetime import datetime

import unittest
import pytest

from tests.test_helpers import TestHelpers
from repositories.user_repository import user_repository
from repositories.workout_repository import workout_repository
from entities.user import User
from entities.workout import Workout
from services.workout_service import workout_service, WorkOutDurationError
from services.user_service import user_service


class TestWorkoutService(unittest.TestCase):
    def setUp(self):
        self.test_helpers = TestHelpers()
        workout_repository.delete_all()
        user_repository.delete_all()
        self.user_matti = User("matti", "password")
        self.workout = Workout("matti", "cardio", 60, datetime.now())
        self.workout_duration_error = WorkOutDurationError()

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

    def test_create_workout_duration_not_a_number(self):
        new_user = user_service.create_user(self.user_matti.username,
                                            self.user_matti.password,
                                            self.user_matti.password)
        user_service.login_user(new_user.username,
                                                 new_user.password)

        with pytest.raises(WorkOutDurationError) as error:
            workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 "text")
        self.assertEqual(str(error.value),
                         "Please enter a valid number for workout duration.")
        
    def test_create_workout_duration_negative_number(self):
        new_user = user_service.create_user(self.user_matti.username,
                                            self.user_matti.password,
                                            self.user_matti.password)
        user_service.login_user(new_user.username,
                                                 new_user.password)

        with pytest.raises(WorkOutDurationError) as error:
            workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 -1)
        self.assertEqual(str(error.value),
                         self.workout_duration_error.message)
        
    def test_create_workout_duration_too_big(self):
        new_user = user_service.create_user(self.user_matti.username,
                                            self.user_matti.password,
                                            self.user_matti.password)
        user_service.login_user(new_user.username,
                                                 new_user.password)

        with pytest.raises(WorkOutDurationError) as error:
            workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 10081)
        self.assertEqual(str(error.value),
                         self.workout_duration_error.message)

    def test_create_workout(self):
        user = user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        workout = workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 self.workout.duration)
        self.test_helpers.check_workout_equality(workout, self.workout)
        self.assertEqual(workout.username, user.username)

    def test_update_workout_duration_negative_number(self):
        new_user = user_service.create_user(self.user_matti.username,
                                            self.user_matti.password,
                                            self.user_matti.password)
        user_service.login_user(new_user.username,
                                                 new_user.password)
        
        new_workout = workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 self.workout.duration)
        
        new_workout.duration = -1

        with pytest.raises(WorkOutDurationError) as error:
            workout_service.update_workout(new_workout)
        self.assertEqual(str(error.value),
                         self.workout_duration_error.message)
        
    def test_update_workout_duration_too_big(self):
        new_user = user_service.create_user(self.user_matti.username,
                                            self.user_matti.password,
                                            self.user_matti.password)
        user_service.login_user(new_user.username,
                                                 new_user.password)
        
        new_workout = workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 self.workout.duration)
        
        new_workout.duration = 10081

        with pytest.raises(WorkOutDurationError) as error:
            workout_service.update_workout(new_workout)
        self.assertEqual(str(error.value),
                         self.workout_duration_error.message)

    def test_update_workout(self):
        user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        new_workout = workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 self.workout.duration)
        new_workout.type = "strength"
        new_workout.duration = 120
        
        workout_service.update_workout(new_workout)
        workout_by_id = workout_service.get_workout_by_id(new_workout.id)

        self.assertEqual(workout_by_id.type, "strength")
        self.assertEqual(workout_by_id.duration, 120)

    def test_delete_workout(self):
        user_service.create_user(self.user_matti.username,
                                        self.user_matti.password,
                                        self.user_matti.password)
        new_workout = workout_service.create_workout(self.user_matti.username,
                                                 self.workout.type,
                                                 self.workout.duration)

        workout_by_id = workout_service.get_workout_by_id(new_workout.id)

        self.assertEqual(workout_by_id.username, self.user_matti.username)

        workout_service.delete_workout(new_workout.id)
        workout_by_id = workout_service.get_workout_by_id(new_workout.id)

        self.assertEqual(workout_by_id, None)

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
