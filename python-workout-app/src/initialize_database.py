from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS workouts;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            username TEXT UNIQUE PRIMARY KEY,
            password TEXT,
            weekly_training_goal_in_minutes INTEGER
        );
    ''')

    cursor.execute('''
        CREATE TABLE workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            type TEXT,
            duration INTEGER,
            created_at DATETIME,
            FOREIGN KEY (username) REFERENCES users (username)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
