from modules.file_handler import read_data, write_data
from utils.helper import print_header, print_success, print_error


TABLE_FILE = "app/database/tables.json"


# ================= BOOK TABLE =================

def book_table():

    print_header("TABLE BOOKING SYSTEM")

    tables = read_data(TABLE_FILE)


    try:
        booking_id = int(input("Enter Booking ID : "))
        table_no = int(input("Enter Table Number (1-10) : "))

    except ValueError:
        print_error("Enter Numeric Value Only")
        return


    if table_no < 1 or table_no > 10:

        print_error("Only Table 1 To 10 Available")
        return


    customer_name = input("Enter Customer Name : ")
    mobile = input("Enter Mobile Number : ")



    for table in tables:

        if table["booking_id"] == booking_id:

            print_error("Booking ID Already Exists")
            return


        if table["table_no"] == table_no:

            print_error("Table Already Booked")
            return



    booking = {

        "booking_id": booking_id,
        "customer_name": customer_name,
        "mobile": mobile,
        "table_no": table_no,
        "status": "Booked"

    }


    tables.append(booking)

    write_data(TABLE_FILE, tables)


    print_success("Table Booked Successfully")





# ================= VIEW BOOKINGS =================


def view_bookings():

    print_header("ALL TABLE BOOKINGS")


    tables = read_data(TABLE_FILE)


    if len(tables) == 0:

        print_error("No Booking Available")
        return



    print(f"\nTotal Bookings : {len(tables)}")



    for table in tables:


        print("\n"+"="*45)

        print("TABLE BOOKING DETAILS".center(45))

        print("="*45)


        print(f"Booking ID   : {table['booking_id']}")
        print(f"Customer     : {table['customer_name']}")
        print(f"Mobile       : {table['mobile']}")
        print(f"Table No     : {table['table_no']}")
        print(f"Status       : {table['status']}")


        print("="*45)







# ================= UPDATE BOOKING =================


def update_booking():

    print_header("UPDATE BOOKING")


    tables = read_data(TABLE_FILE)



    try:

        booking_id = int(input("Enter Booking ID : "))

    except ValueError:

        print_error("Invalid Booking ID")
        return





    for table in tables:


        if table["booking_id"] == booking_id:


            print("\nCurrent Details")
            print("-"*30)

            print(
                f"Customer : {table['customer_name']}"
            )

            print(
                f"Mobile : {table['mobile']}"
            )

            print(
                f"Table : {table['table_no']}"
            )


            print("-"*30)



            table["customer_name"] = input(
                "New Customer Name : "
            )


            table["mobile"] = input(
                "New Mobile Number : "
            )



            try:

                new_table = int(
                    input("New Table Number : ")
                )


            except ValueError:

                print_error("Invalid Table Number")
                return



            table["table_no"] = new_table



            write_data(
                TABLE_FILE,
                tables
            )


            print_success(
                "Booking Updated Successfully"
            )


            return




    print_error("Booking Not Found")








# ================= CANCEL BOOKING =================


def cancel_booking():


    print_header("CANCEL BOOKING")


    tables = read_data(TABLE_FILE)



    try:

        booking_id = int(
            input("Enter Booking ID : ")
        )


    except ValueError:

        print_error("Invalid Booking ID")
        return




    for table in tables:


        if table["booking_id"] == booking_id:



            confirm = input(
                "Cancel Booking? (Y/N) : "
            )



            if confirm.upper() == "Y":


                tables.remove(table)


                write_data(
                    TABLE_FILE,
                    tables
                )


                print_success(
                    "Booking Cancelled Successfully"
                )


            else:

                print("Cancellation Cancelled")



            return




    print_error("Booking Not Found")