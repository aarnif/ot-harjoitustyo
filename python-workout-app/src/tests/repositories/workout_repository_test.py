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
        self.workout = Workout("matti", "cardio", 60, datetime.now())
        user_repository.create(self.user_matti)

    def test_create_workout(self):
        workout = workout_repository.create(self.workout)
        self.test_helpers.check_workout_equality(workout, self.workout)

    def test_find_all_workouts_by_username(self):
        workouts = workout_repository.find_all_by_username(
            self.user_matti.username)
        self.assertEqual(workouts, [])
        workout_repository.create(self.workout)
        workouts = workout_repository.find_all_by_username(
            self.user_matti.username)
        self.test_helpers.check_workout_equality(workouts[0], self.workout)

    def test_find_one_workout_by_username(self):
        workout = workout_repository.find_one_by_username(
            self.user_matti.username)
        self.assertEqual(workout, None)
        workout_repository.create(self.workout)
        workout = workout_repository.find_one_by_username(
            self.user_matti.username)
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
