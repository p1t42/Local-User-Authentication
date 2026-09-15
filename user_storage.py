from pathlib import Path
import json

def get_stored_user_info(path):
    """Read the stored user data from the JSON file.

    Returns the list of users, or None if the file does not exist.
    """
    if path.exists():
        user_contents = path.read_text()
        user_info = json.loads(user_contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Ask for a new user's name and password and append it to the stored user data."""
    user_name = input("\nPlease Enter your first name: ")
    user_password = input("Please Enter a new password: ")
    # defoult data storing structure
    new_user = {"User info:": [user_name, user_password]}
    user_info = get_stored_user_info(path)
    if user_info:
        user_info.append(new_user)
    else:
        user_info = [new_user]
    contents = json.dumps(user_info)
    #appending new data 
    path.write_text(contents)
    print("Your Info is saved")
    
def login(path):
    """Prompt for a name and password and verify them against the stored users."""
    print("\nPlease log in")
    name = input("\tName: ")
    password = input("\tPassword: ")
    user_info = get_stored_user_info(path)
    # Flatten the list of user dicts into a list of [name password] pairs:
    users = []
    for user in user_info:
        users.append(user["User info:"]) # adds the name password pairs to users
    for user in users:
        if user[0] == name and user[1] == password:
            print(f"Welcome back {name.title()}")
        elif user[0] != name:
            print("The name doesn't match")
            break
        elif user[1] != password:
            print("The password doesn't match")
            break

def append_new_user(path):
    """Add a new user to the stored data by calling get_new_user_info."""
    get_new_user_info(path)
    print("Adding you to all users...")


def greet_user(): 
    """Entry point: greet the user, then either create a new user or log in an existing one."""
    path = Path("user_data/user_data.json")
    user_info = get_stored_user_info(path)
    if user_info:
        print("\nDo you want to create a new user or log in?")
        print("log in / create new user")
        user_input = input("\n")
        lower_user_input = user_input.lower()
        if lower_user_input == "log in":
            login(path)
        elif lower_user_input == "create new user":
            append_new_user(path)
        else: 
            print("Invalid command")
    else:
        get_new_user_info(path)