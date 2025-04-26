from datetime import datetime

from entities.workout import Workout
from repositories.workout_repository import (
    workout_repository as default_workout_repository
)


class WorkOutDurationError(Exception):
    """Poikkeus, joka heitetään, jos treenin keston arvo on virheellinen.

    Args:
        message (str, optional): Virheilmoituksen viesti. Oletusarvo "Workout duration must be number between 1 and 10080."
    """
    def __init__(self, message="Workout duration must be number between 1 and 10080."):
        self.message = message
        super().__init__(self.message)


class WorkoutService:
    """Treeneihin liittyvästä sovelluslogiikasta vastaava luokka.
    """
    def __init__(self, workout_repository=default_workout_repository):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            workout_repository (WorkoutRepository, optional): Olio, joka omaa WorkoutRepository-luokkaa vastaavat metodit. Oletusarvo WorkoutRepository-olio.
        """
        self.workout_repository = workout_repository

    def _validate_duration(self, duration):
        """Validoi treenin keston arvon.

        Args:
            duration (int): Treenin kesto minuutteina

        Raises:
            WorkOutDurationError: Treenin kesto on negatiivinen luku
            WorkOutDurationError: Treenin kesto on liian suuri luku

        Returns:
            int: Validoitu treenin kesto minuutteina
        """
        if isinstance(duration, str):
            duration = int(duration)

        if duration <= 0:
            raise WorkOutDurationError()
        # Maximum minutes in a week (7*24*60)
        if duration > 10080:
            raise WorkOutDurationError()

        return duration

    def get_all_user_workouts(self, username):
        """Palauttaa kaikki käyttäjän treenit.

        Args:
            username (str): Käyttäjätunnus

        Returns:
            list[Workout]: Lista käyttäjän treeneistä Workout-olioina
        """
        workouts = self.workout_repository.find_all_by_username(username)
        return workouts

    def get_workout_by_id(self, workout_id):
        """Palauttaa yksittäisen treenin id:n perusteella.

        Args:
            workout_id (str): Treenin id

        Returns:
            Workout: Workout-olio, joka vastaa annettua treenin id:tä
        """
        workout = self.workout_repository.find_one_by_id(workout_id)
        return workout

    def create_workout(self, username, workout_type, workout_duration):
        """Luo uuden treenin.

        Args:
            username (str): Käyttäjätunnus
            workout_type (str): Treenin tyyppi
            workout_duration (int): Treenin kesto minuutteina

        Raises:
            WorkOutDurationError: Treenin kesto ei ole luku

        Returns:
            Workout: Luotu treeni joka on Workout-olio
        """
        try:
            workout_duration = self._validate_duration(workout_duration)

            created_workout = self.workout_repository.create(
                Workout(username, workout_type, workout_duration, datetime.now()))
            return created_workout

        except ValueError as exc:
            raise WorkOutDurationError(
                "Please enter a valid number for workout duration.") from exc

    def update_workout(self, workout):
        """Päivittää olemassa olevan treenin.

        Args:
            workout (Workout): Treeni joka halutaan päivittää Workout-oliona

        Raises:
            WorkOutDurationError: Treenin kesto ei ole luku

        Returns:
            Workout: Päivitetty treeni joka on Workout-olio
        """
        try:
            validated_duration = self._validate_duration(workout.duration)
            workout.duration = validated_duration

            updated_workout = self.workout_repository.update(workout)
            return updated_workout

        except ValueError as exc:
            raise WorkOutDurationError(
                "Please enter a valid number for workout duration.") from exc

    def delete_workout(self, workout_id):
        """Poistaa treenin id:n perusteella.

        Args:
            workout_id (str): Treenin id

        Returns:
            Bool: True, jos treeni poistettiin onnistuneesti, muuten False
        """
        return self.workout_repository.delete(workout_id)

    def get_weeks_workout_total(self, username):
        """Laskee käyttäjän treenien kokonaiskeston nykyiseltä viikolta.

        Args:
            username (str): Käyttäjätunnus

        Returns:
            int: Käyttäjän treenien kokonaiskesto nykyiseltä viikolta minuutteina
        """
        workout_total = self.workout_repository.get_current_weeks_workout_total(
            username)
        return workout_total


workout_service = WorkoutService()
