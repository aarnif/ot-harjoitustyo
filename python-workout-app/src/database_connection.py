import os
from datetime import datetime
import sqlite3
from config import DATABASE_FILENAME

# generoitu koodi alkaa


def adapt_datetime(dt: datetime) -> str:
    return dt.isoformat(" ")


def convert_datetime(s: bytes) -> datetime:
    return datetime.fromisoformat(s.decode())


sqlite3.register_adapter(datetime, adapt_datetime)
sqlite3.register_converter("datetime", convert_datetime)
# generoitu koodi päättyy

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", DATABASE_FILENAME))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
