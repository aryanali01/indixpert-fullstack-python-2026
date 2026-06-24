from modules.auth import sign_up, sign_in

from modules.menu import *
from modules.customer import *
from modules.table import *
from modules.order import *
from modules.billing import *
from modules.staff import *
from modules.reports import *
from modules.profile import *

from utils.helper import (
    print_header,
    print_success,
    print_error
)



# ================= MENU MANAGEMENT =================

def menu_management():

    while True:

        print_header("ALVI MENU MANAGEMENT")

        print("1. Add Item")
        print("2. View Items")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Back")


        choice=input("\nEnter Choice : ")



        if choice=="1":
            add_item()

        elif choice=="2":
            view_items()

        elif choice=="3":
            search_item()

        elif choice=="4":
            update_item()

        elif choice=="5":
            delete_item()

        elif choice=="6":
            break

        else:
            print_error("Invalid Choice")





# ================= CUSTOMER =================


def customer_management():

    while True:

        print_header("CUSTOMER MANAGEMENT")


        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back")


        choice=input("\nEnter Choice : ")


        if choice=="1":
            add_customer()

        elif choice=="2":
            view_customers()

        elif choice=="3":
            search_customer()

        elif choice=="4":
            update_customer()

        elif choice=="5":
            delete_customer()

        elif choice=="6":
            break

        else:
            print_error("Invalid Choice")





# ================= TABLE =================


def table_management():

    while True:

        print_header("TABLE BOOKING")


        print("1. Book Table")
        print("2. View Booking")
        print("3. Update Booking")
        print("4. Cancel Booking")
        print("5. Back")


        choice=input("\nEnter Choice : ")



        if choice=="1":
            book_table()

        elif choice=="2":
            view_bookings()

        elif choice=="3":
            update_booking()

        elif choice=="4":
            cancel_booking()

        elif choice=="5":
            break

        else:
            print_error("Invalid Choice")





# ================= ORDER =================


def order_management():

    while True:

        print_header("ORDER MANAGEMENT")


        print("1. Place Order")
        print("2. View Orders")
        print("3. Update Order")
        print("4. Cancel Order")
        print("5. Back")


        choice=input("\nEnter Choice : ")



        if choice=="1":
            place_order()

        elif choice=="2":
            view_orders()

        elif choice=="3":
            update_order()

        elif choice=="4":
            cancel_order()

        elif choice=="5":
            break

        else:
            print_error("Invalid Choice")





# ================= BILLING =================


def billing_management():

    while True:

        print_header("BILLING SYSTEM")


        print("1. Generate Bill")
        print("2. View Bills")
        print("3. Payment")
        print("4. Bill History")
        print("5. Back")


        choice=input("\nEnter Choice : ")



        if choice=="1":
            generate_bill()

        elif choice=="2":
            view_bills()

        elif choice=="3":
            payment()

        elif choice=="4":
            bill_history()

        elif choice=="5":
            break

        else:
            print_error("Invalid Choice")





# ================= STAFF =================


def staff_management():

    while True:

        print_header("STAFF MANAGEMENT")


        print("1. Add Staff")
        print("2. View Staff")
        print("3. Update Staff")
        print("4. Delete Staff")
        print("5. Back")


        choice=input("\nEnter Choice : ")



        if choice=="1":
            add_staff()

        elif choice=="2":
            view_staff()

        elif choice=="3":
            update_staff()

        elif choice=="4":
            delete_staff()

        elif choice=="5":
            break

        else:
            print_error("Invalid Choice")





# ================= REPORT =================


def reports_menu():

    while True:

        print_header("REPORT SYSTEM")


        print("1. Total Customers")
        print("2. Total Orders")
        print("3. Total Sales")
        print("4. Total Staff")
        print("5. Total Tables")
        print("6. Total Bills")
        print("7. Revenue")
        print("8. Top Item")
        print("9. Business Summary")
        print("10. Back")


        choice=input("\nEnter Choice : ")



        if choice=="1":
            total_customers()

        elif choice=="2":
            total_orders()

        elif choice=="3":
            total_sales()

        elif choice=="4":
            total_staff()

        elif choice=="5":
            total_tables()

        elif choice=="6":
            total_bills()

        elif choice=="7":
            total_revenue()

        elif choice=="8":
            most_ordered_item()

        elif choice=="9":
            business_summary()

        elif choice=="10":
            break

        else:
            print_error("Invalid Choice")






# ================= PROFILE =================


def profile_menu():

    while True:

        print_header("PROFILE")


        print("1. View Profile")
        print("2. Update Profile")
        print("3. Change Password")
        print("4. Back")


        choice=input("\nEnter Choice : ")



        if choice=="1":
            view_profile()

        elif choice=="2":
            update_profile()

        elif choice=="3":
            change_password()

        elif choice=="4":
            break

        else:
            print_error("Invalid Choice")






# ================= DASHBOARD =================


def dashboard():


    while True:


        print_header(
            "ALVI ROYAL RESTAURANT MANAGEMENT"
        )


        print("1. Menu Management")
        print("2. Customer Management")
        print("3. Table Booking")
        print("4. Order Management")
        print("5. Billing System")
        print("6. Staff Management")
        print("7. Reports")
        print("8. Profile")
        print("9. Logout")


        choice=input("\nEnter Choice : ")



        if choice=="1":

            menu_management()


        elif choice=="2":

            customer_management()


        elif choice=="3":

            table_management()


        elif choice=="4":

            order_management()


        elif choice=="5":

            billing_management()


        elif choice=="6":

            staff_management()


        elif choice=="7":

            reports_menu()


        elif choice=="8":

            profile_menu()


        elif choice=="9":

            print_success(
                "Logout Successful"
            )

            break


        else:

            print_error(
                "Invalid Choice"
            )







# ================= MAIN =================



while True:


    print_header(
        "ALVI ROYAL RESTAURANT MANAGEMENT SYSTEM"
    )


    print("1. Sign Up")
    print("2. Sign In")
    print("3. Exit")


    choice=input("\nEnter Choice : ")



    if choice=="1":

        sign_up()



    elif choice=="2":


        login=sign_in()


        if login:

            dashboard()




    elif choice=="3":


        print_success(
            "Thank You"
        )

        break



    else:

        print_error(
            "Invalid Choice"
        )