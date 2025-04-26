from datetime import datetime, timedelta

from entities.workout import Workout
from database_connection import get_database_connection


def get_workout_from_row(row):
    """Muodostaa Workout-olion tietokannan rivistä.

    Args:
        row (dict | None): Tietokannan rivi, joka sisältää treenitiedot. Voi olla None jos treeniä ei löydy.

    Returns:
        Workout | None: Workout-olio, joka vastaa tietokannan riviä, tai None jos riviä ei löydy.
    """
    if row:
        return Workout(row["username"], row["type"], row["duration"], row["created_at"], row["id"])

    return None


class WorkoutRepository:
    """Luokka, joka vastaa treeneihin liittyvistä tietokantatoiminnoista.
    """
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection (sqlite3.Connection): Tietokantayhteys
        """
        self._connection = connection

    def delete_all(self):
        """Poistaa kaikki treenit tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM workouts")
        self._connection.commit()

    def find_all_by_username(self, username):
        """Hakee kaikki käyttäjän treenit tietokannasta.

        Returns:
            list[Workout]: Lista kaikista käyttäjän Workout-olioista
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, username, type, duration, created_at FROM workouts WHERE username = ?",
            (username,))

        rows = cursor.fetchall()

        workouts = [get_workout_from_row(row) for row in rows]

        return workouts

    def find_one_by_id(self, workout_id):
        """Hakee treenin tietokannasta treenin id:n perusteella.

        Args:
            workout_id (str): Treenin id

        Returns:
            Workout: Workout-olio, joka vastaa tietokannan riviä
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, username, type, duration, created_at FROM workouts WHERE id = ?",
            (workout_id,))

        row = cursor.fetchone()

        workout = get_workout_from_row(row)

        return workout

    def create(self, workout):
        """Luo uuden treenin tietokantaan.

        Args:
            user (Workout): Workout-olio, joka halutaan luoda

        Returns:
            Workout: Luotu Workout-olio
        """
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
        """Päivittää olemassa olevan treenin tietokannassa.

        Args:
            workout (Workout): Workout-olio, joka halutaan päivittää

        Returns:
            Workout: Päivitetty Workout-olio
        """
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
        """Poistaa yksittäisen treenin tietokannasta sen id:n perusteella.

        Args:
            workout_id (str): Treenin id

        Returns:
            bool: True, jos treeni poistettiin onnistuneesti, muuten False
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "DELETE FROM workouts WHERE id = ?",
            (workout_id,)
        )
        self._connection.commit()
        return cursor.rowcount > 0

    def get_current_weeks_workout_total(self, username):
        """Laskee käyttäjän treenien kokonaiskeston nykyiseltä viikolta.

        Args:
            username (str): Käyttäjätunnus

        Returns:
            int: Käyttäjän treenien kokonaiskesto nykyiseltä viikolta minuuteissa
        """
        cursor = self._connection.cursor()
        
        today = datetime.now()
        
        start_of_week = today - timedelta(days=today.weekday())
        start_of_week = datetime(
            start_of_week.year, start_of_week.month, start_of_week.day)
        start_of_week_str = start_of_week.strftime("%Y-%m-%d %H:%M:%S")
        
        end_of_week = start_of_week + timedelta(days=6)
        end_of_week = datetime(
            end_of_week.year, end_of_week.month, end_of_week.day, 23, 59, 59)
        end_of_week_str = end_of_week.strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute(
            """
            SELECT SUM(duration) as workout_total 
            FROM workouts 
            WHERE username = ? 
            AND created_at BETWEEN ? AND ?
            """,
            (username, start_of_week_str, end_of_week_str)
        )
        
        result = cursor.fetchone()
        if result["workout_total"]:
            return int(result["workout_total"])
        return 0
    # generoitu koodi päättyy


workout_repository = WorkoutRepository(get_database_connection())
