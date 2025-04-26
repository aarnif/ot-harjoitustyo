class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.

    Attributes:
        username (str): Käyttäjänimi
        password (str): Käyttäjän salasana
        weekly_training_goal_in_minutes (int): Käyttäjän viikoittainen treenitavoite minuutteina
    """
    def __init__(self, username, password, weekly_training_goal_in_minutes=0):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username (str): Käyttäjänimi
            password (str): Käyttäjän salasana
            weekly_training_goal_in_minutes (int, optional): Käyttäjän viikoittainen treenitavoite minuutteina. Oletusarvo 0.
        """
        self.username = username
        self.password = password
        self.weekly_training_goal_in_minutes = weekly_training_goal_in_minutes
