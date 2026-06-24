from modules.file_handler import read_data, write_data
from utils.helper import print_header, print_success, print_error


STAFF_FILE = "app/database/staff.json"



# ================= ADD STAFF =================

def add_staff():

    print_header("ADD STAFF")

    staffs = read_data(STAFF_FILE)


    try:
        staff_id = int(input("Enter Staff ID : "))

    except ValueError:
        print_error("Staff ID Must Be Number")
        return



    name = input("Enter Staff Name : ")
    role = input("Enter Role : ")


    try:
        salary = float(input("Enter Salary : "))

    except ValueError:
        print_error("Invalid Salary")
        return





    for staff in staffs:

        if staff["staff_id"] == staff_id:

            print_error("Staff ID Already Exists")

            return




    staff = {

        "staff_id": staff_id,
        "name": name,
        "role": role,
        "salary": salary

    }




    staffs.append(staff)


    write_data(STAFF_FILE,staffs)


    print_success("Staff Added Successfully")








# ================= VIEW STAFF =================


def view_staff():

    print_header("STAFF MANAGEMENT")


    staffs = read_data(STAFF_FILE)



    if len(staffs) == 0:

        print_error("No Staff Found")

        return





    print(f"\nTotal Staff : {len(staffs)}")



    for staff in staffs:


        print("\n"+"="*45)

        print("STAFF DETAILS".center(45))

        print("="*45)


        print(f"Staff ID : {staff['staff_id']}")


        print(f"Name     : {staff['name']}")


        print(f"Role     : {staff['role']}")


        print(f"Salary   : ₹{staff['salary']}")


        print("="*45)









# ================= UPDATE STAFF =================


def update_staff():


    print_header("UPDATE STAFF")


    staffs = read_data(STAFF_FILE)



    try:

        staff_id = int(input("Enter Staff ID : "))


    except ValueError:

        print_error("Invalid Staff ID")

        return






    for staff in staffs:



        if staff["staff_id"] == staff_id:




            staff["name"] = input("New Name : ")


            staff["role"] = input("New Role : ")



            try:

                staff["salary"] = float(input("New Salary : "))


            except ValueError:

                print_error("Invalid Salary")

                return





            write_data(STAFF_FILE,staffs)



            print_success("Staff Updated Successfully")


            return





    print_error("Staff Not Found"
)









# ================= DELETE STAFF =================


def delete_staff():


    print_header("DELETE STAFF")


    staffs = read_data(STAFF_FILE)



    try:

        staff_id = int(input("Enter Staff ID : "))


    except ValueError:

        print_error("Invalid Staff ID")

        return





    for staff in staffs:



        if staff["staff_id"] == staff_id:




            print("\nStaff Details")

            print("-"*30)


            print("Name :",staff["name"])

            print("Role :",staff["role"])


            print("-"*30)



            confirm = input("Delete Staff? (Y/N) : ")




            if confirm.upper() == "Y":


                staffs.remove(staff)


                write_data(STAFF_FILE,staffs)


                print_success("Staff Deleted Successfully")


            else:

                print("Delete Cancelled")



            return





    print_error("Staff Not Found")