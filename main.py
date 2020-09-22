import getpass

from database_operations import exist_db, add_user_to_db, is_valid_credentials
from security import check_auth
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
            database_name = input("Enter database name: \n")
            exist_db(db_name=database_name)
            quit_button = input("To go BACK, press 'Q'. Continue, press ENTER")
    elif option == "2":
        while quit_button != "Q":
            username = input("Enter username: \n")
            password = getpass.getpass("Enter password: \n")
            add_user_to_db(username=username, password=password)
            quit_button = input("To go BACK, press 'Q'. Continue, press ENTER")
    elif option == "3":
        username = input("Enter username: \n")
        password = getpass.getpass("Enter password: \n")
        security_code = input("Enter security code: \n")
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


