class Workout:
    """Luokka, joka kuvaa käyttäjän yksittäistä treeniä.

    Attributes:
        id (int): Treenin id
        username (str): Käyttäjänimi, joka on treenin luoja
        type (str): Treenin tyyppi
        duration (int): Treenin kesto minuutteina
        created_at (datetime): Treenin luontiaika
    """

    def __init__(self, username, workout_type, workout_duration, created_at, workout_id=None):
        """Luokan konstruktori, joka luo uuden treenin.

        Args:
            username (str): Käyttäjänimi, joka on treenin luoja
            workout_type (str): Treenin tyyppi
            workout_duration (str): Treenin kesto minuutteina
            created_at (str): Treenin luontiaika
            workout_id (int, optional): Treenin id. Oletusarvo None, 
            ennen kuin treeni tallennetaan tietokantaan.
        """
        self.id = workout_id
        self.username = username
        self.type = workout_type
        self.duration = workout_duration
        self.created_at = created_at
