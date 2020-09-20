from security import check_auth, hash_user_password
from database_operations import exist_db, create_new_db, select_user_from_db, add_user_to_db, is_valid_credentials

import getpass

# Start by checking to see whether the ppab6.db database already exists
    # def db_exists(db_name) - CHECK
# If it does, ask the user if they want to delete and recreate it.
# Maybe tell them what tables it has and how many rows each one has
# so that they understand the consequences of their actions (you’ll have to look up how to do this)
    # def delete_db(db_name)
    # def recreate_db(db_name)
    # def explain_db(db_name) -> what is db and how many rows has
from user import User


def welcome_screen():
    quit_button = None
    print("Welcome in the great application!")
    print("What do you want to do?")
    option = input("Check if database exist - select 1\n"
                   "Create user account - select 2\n"
                   "Login to the great application - select 3\n")
    if option == "1":
        while quit_button != "Q":
            database_name = input("Podaj nazwę bazy danych: \n")
            exist_db(db_name=database_name)
            quit_button = input("Aby powrócić do poprzedniego menu wybierz 'Q. Aby kontunuować, wybierz ENTER")
    elif option == "2":
        while quit_button != "Q":
            username = input("Podaj nazwe uzytkownika: \n")
            password = getpass.getpass("Podaj haslo: \n")
            add_user_to_db(username=username, password=password)
            quit_button = input("Aby powrócić do poprzedniego menu wybierz 'Q'. Aby kontunuować, wybierz ENTER")
    elif option == "3":
        username = input("Podaj nazwe uzytkownika: \n")
        password = getpass.getpass("Podaj haslo: \n")
        security_code = input("Podaj kod bezpieczenstwa: \n")
        login(username=username, password=password, security_code=security_code)
    else:
        print("Wrong option")


def login(username, password, security_code):
    if is_valid_credentials(username, password):
        if check_auth(security_code):
            print("Your are logged in")
            user = User(name=username)
            print(user)
        else:
            quit()
    else:
        print("Wrong credentials")


if __name__ == '__main__':
    welcome_screen()


