from modules.file_handler import read_data, write_data
from utils.validation import validate_password
from utils.helper import print_header, print_success, print_error


USER_FILE = "app/database/users.json"


# ================= VIEW PROFILE =================

def view_profile():

    print_header("USER PROFILE")

    users = read_data(USER_FILE)

    username = input("Enter Username : ")

    for user in users:

        if user["username"] == username:

            print("\n" + "=" * 50)
            print("PROFILE DETAILS".center(50))
            print("=" * 50)

            print(f"User ID       : {user['id']}")
            print(f"Full Name     : {user['full_name']}")
            print(f"DOB           : {user['dob']}")
            print(f"Address       : {user['address']}")
            print(f"Qualification : {user['qualification']}")
            print(f"Username      : {user['username']}")

            print("=" * 50)

            return

    print_error("User Not Found")


# ================= UPDATE PROFILE =================

def update_profile():

    print_header("UPDATE PROFILE")

    users = read_data(USER_FILE)

    username = input("Enter Username : ")

    for user in users:

        if user["username"] == username:

            print("\nCurrent Profile")
            print("-" * 40)

            print(f"Name          : {user['full_name']}")
            print(f"DOB           : {user['dob']}")
            print(f"Address       : {user['address']}")
            print(f"Qualification : {user['qualification']}")

            print("-" * 40)

            user["full_name"] = input("New Full Name : ")
            user["dob"] = input("New DOB : ")
            user["address"] = input("New Address : ")
            user["qualification"] = input("New Qualification : ")

            write_data(USER_FILE, users)

            print_success("Profile Updated Successfully")

            return

    print_error("User Not Found")


# ================= CHANGE PASSWORD =================

def change_password():

    print_header("CHANGE PASSWORD")

    users = read_data(USER_FILE)

    username = input("Enter Username : ")

    for user in users:

        if user["username"] == username:

            old_password = input("Enter Old Password : ")

            if user["password"] != old_password:

                print_error("Incorrect Old Password")

                return

            new_password = input("Enter New Password : ")

            if not validate_password(new_password):

                print_error("Password Must Be At Least 6 Characters")

                return

            confirm_password = input("Confirm New Password : ")

            if new_password != confirm_password:

                print_error("Passwords Do Not Match")

                return

            user["password"] = new_password

            write_data(USER_FILE,users)

            print_success("Password Changed Successfully")

            return
        
        print_error("User Not Found")