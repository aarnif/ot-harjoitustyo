from datetime import datetime
import unittest

from tests.test_helpers import TestHelpers
from repositories.user_repository import user_repository
from repositories.workout_repository import workout_repository
from entities.user import User
from entities.workout import Workout


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.test_helpers = TestHelpers()
        workout_repository.delete_all()
        user_repository.delete_all()
        self.user_matti = User("matti", "password", 600)
        self.workout = Workout("matti", "Cardio", 60, datetime.now())
        user_repository.create(self.user_matti)

    def test_create_workout(self):
        workout = workout_repository.create(self.workout)
        self.test_helpers.check_workout_equality(workout, self.workout)

    def test_update_workout(self):
        new_workout = workout_repository.create(self.workout)
        self.assertEqual(new_workout.duration, self.workout.duration)
        new_workout.duration = 120
        updated_workout = workout_repository.update(new_workout)
        self.assertEqual(updated_workout.duration, 120)

    def test_delete_workout(self):
        new_workout = workout_repository.create(self.workout)
        self.test_helpers.check_workout_equality(new_workout, self.workout)
        workout_is_deleted = workout_repository.delete(new_workout.id)
        self.assertEqual(workout_is_deleted, True)

    def test_find_all_workouts_by_username(self):
        workouts = workout_repository.find_all_by_username(
            self.user_matti.username)
        self.assertEqual(workouts, [])
        workout_repository.create(self.workout)
        workouts = workout_repository.find_all_by_username(
            self.user_matti.username)
        self.test_helpers.check_workout_equality(workouts[0], self.workout)

    def test_find_one_workout_by_id(self):
        workout = workout_repository.create(self.workout)
        workout = workout_repository.find_one_by_id(
            workout.id)

        self.test_helpers.check_workout_equality(workout, self.workout)

    def test_get_weeks_workout_total(self):
        total = workout_repository.get_current_weeks_workout_total(
            self.user_matti.username)
        self.assertEqual(total, 0)
        workout_repository.create(self.workout)
        workout_repository.create(self.workout)
        total = workout_repository.get_current_weeks_workout_total(
            self.user_matti.username)
        self.assertEqual(total, 120)
