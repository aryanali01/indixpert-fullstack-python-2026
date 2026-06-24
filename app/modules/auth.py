from modules.file_handler import read_data, write_data
from utils.validation import validate_password
from utils.helper import generate_user_id

USER_FILE = "app/database/users.json"

# ================= HEADER =================

def header(title):
    print("\n" + "═" * 80)
    print(title.center(80))
    print("═" * 80)


# ================= SIGN UP =================

def sign_up():

    header("PLEASE CREATE NEW ACCOUNT")

    users = read_data(USER_FILE)

    full_name = input("Full Name      : ").strip()
    dob = input("Date Of Birth  : ").strip()
    address = input("Address        : ").strip()
    qualification = input("Qualification  : ").strip()
    username = input("Username       : ").strip()

    if not full_name:
        print("Name Cannot Be Empty")
        return

    if len(username) < 4:
        print("Username Must Be At Least 4 Characters")
        return

    for user in users:

        if user["username"].lower() == username.lower():

            print("Username Already Exists")
            return

    print("\nPassword Rules")
    print("- Minimum 6 Characters")

    password = input("Password       : ")

    if not validate_password(password):

        print("Password Must Be At Least 6 Characters")
        return
    
    user = {
        "id": generate_user_id(users),
        "full_name": full_name,
        "dob": dob,
        "address": address,
        "qualification": qualification,
        "username": username,
        "password": password
    }

    users.append(user)

    write_data(USER_FILE, users)

    print("\n" + "═" * 50)
    print("ACCOUNT CREATED SUCCESSFULLY")
    print("═" * 50)

    print(f"User ID        : {user['id']}")
    print(f"Name           : {full_name}")
    print(f"Username       : {username}")
    print(f"Qualification  : {qualification}")

    print("═" * 50)


# ================= SIGN IN =================

def sign_in():

    header("USER LOGIN")

    users = read_data(USER_FILE)

    username = input("Username : ").strip()
    password = input("Password : ")

    for user in users:

        if (
            user["username"].lower() == username.lower()
            and user["password"] == password
        ):

            print("\n" + "═" * 50)
            print("LOGIN SUCCESSFUL")
            print("═" * 50)

            print(f"Welcome : {user['full_name']}")
            print(f"User ID : {user['id']}")

            print("═" * 50)

            return True

    print("\nInvalid Username Or Password")
    return False