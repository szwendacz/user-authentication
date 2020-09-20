import os
import sqlite3

from config import DATABASE_NAME
from security import hash_user_password


# username VARCHAR, password_hash VARCHAR


def create_new_db(db_name, table_name, columns):
    db = sqlite3.connect(db_name + ".db")
    c = db.cursor()
    c.execute(f"CREATE TABLE {table_name} ({columns})")
    db.commit()


def delete_db(db_name):
    try:
        os.remove(db_name + ".db")
        print("Baza danych zostal usunieta")
    except OSError:
        print("Baza danych nie istnieje")


def exist_db(db_name):
    path = db_name + ".db"
    if os.path.exists(path):
        print(f"Baza danych o nazwie {db_name} istnieje w naszej aplikacji")
        return True
    else:
        print(f"Baza danych o nazwie {db_name} nie istnieje w naszej aplikacji")
        return False


def add_user_to_db(username, password):
    db = sqlite3.connect(DATABASE_NAME)
    table_credentials = db.cursor()
    table_credentials.execute(f"INSERT INTO credentials VALUES ('{username}', '{hash_user_password(password=password)}')")
    db.commit()
    table_credentials.close()


def select_user_from_db(username, password):
    db = sqlite3.connect(DATABASE_NAME)
    table_credentials = db.cursor()
    user = table_credentials.execute(f"SELECT username from credentials where username = '{username}' AND password_hash = '{hash_user_password(password=password)}'").fetchone()
    if user is None:
        return False
    else:
        return True


def is_valid_credentials(username, password):
    if select_user_from_db(username, password):
        return True
    else:
        return False