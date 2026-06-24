from modules.file_handler import read_data, write_data
from utils.helper import print_header, print_success, print_error

CUSTOMER_FILE = "app/database/customers.json"


# ================= ADD CUSTOMER =================

def add_customer():

    print_header("ADD CUSTOMER")

    customers = read_data(CUSTOMER_FILE)

    try:
        customer_id = int(input("Enter Customer ID     : "))
    except ValueError:
        print_error("Customer ID Must Be Numeric")
        return

    name = input("Enter Customer Name   : ")
    mobile = input("Enter Mobile Number   : ")
    address = input("Enter Address         : ")

    for customer in customers:

        if customer["id"] == customer_id:

            print_error("Customer ID Already Exists")
            return

    new_customer = {
        "id": customer_id,
        "name": name,
        "mobile": mobile,
        "address": address
    }

    customers.append(new_customer)

    write_data(CUSTOMER_FILE, customers)

    print_success("Customer Added Successfully")


# ================= VIEW CUSTOMERS =================

def view_customers():

    print_header("CUSTOMER LIST")

    customers = read_data(CUSTOMER_FILE)

    if len(customers) == 0:

        print_error("No Customers Found")
        return

    print(f"\nTotal Customers : {len(customers)}\n")

    for customer in customers:

        print("+" + "-" * 42 + "+")
        print("| CUSTOMER INFORMATION".ljust(43) + "|")
        print("+" + "-" * 42 + "+")

        print(f"| ID      : {customer['id']}".ljust(43) + "|")
        print(f"| Name    : {customer['name']}".ljust(43) + "|")
        print(f"| Mobile  : {customer['mobile']}".ljust(43) + "|")
        print(f"| Address : {customer['address']}".ljust(43) + "|")

        print("+" + "-" * 42 + "+")


# ================= SEARCH CUSTOMER =================

def search_customer():

    print_header("SEARCH CUSTOMER")

    customers = read_data(CUSTOMER_FILE)

    mobile = input("Enter Mobile Number : ")

    for customer in customers:

        if customer["mobile"] == mobile:

            print("\n" + "+" + "-" * 42 + "+")
            print("| CUSTOMER FOUND".ljust(43) + "|")
            print("+" + "-" * 42 + "+")

            print(f"| ID      : {customer['id']}".ljust(43) + "|")
            print(f"| Name    : {customer['name']}".ljust(43) + "|")
            print(f"| Mobile  : {customer['mobile']}".ljust(43) + "|")
            print(f"| Address : {customer['address']}".ljust(43) + "|")

            print("+" + "-" * 42 + "+")

            return

    print_error("Customer Not Found")


# ================= UPDATE CUSTOMER =================

def update_customer():

    print_header("UPDATE CUSTOMER")

    customers = read_data(CUSTOMER_FILE)

    try:
        customer_id = int(input("Enter Customer ID : "))
    except ValueError:
        print_error("Customer ID Must Be Numeric")
        return

    for customer in customers:

        if customer["id"] == customer_id:

            print("\nCurrent Details")
            print("-" * 40)

            print(f"Name    : {customer['name']}")
            print(f"Mobile  : {customer['mobile']}")
            print(f"Address : {customer['address']}")

            print("-" * 40)

            customer["name"] = input("Enter New Name    : ")
            customer["mobile"] = input("Enter New Mobile  : ")
            customer["address"] = input("Enter New Address : ")

            write_data(CUSTOMER_FILE, customers)

            print_success("Customer Updated Successfully")

            return

    print_error("Customer Not Found")


# ================= DELETE CUSTOMER =================

def delete_customer():

    print_header("DELETE CUSTOMER")

    customers = read_data(CUSTOMER_FILE)

    try:
        customer_id = int(input("Enter Customer ID : "))
    except ValueError:
        print_error("Customer ID Must Be Numeric")
        return

    for customer in customers:

        if customer["id"] == customer_id:

            print("\nCustomer Found")
            print("-" * 40)

            print(f"ID      : {customer['id']}")
            print(f"Name    : {customer['name']}")
            print(f"Mobile  : {customer['mobile']}")
            print(f"Address : {customer['address']}")

            print("-" * 40)

            confirm = input("Delete This Customer? (Y/N) : ")

            if confirm.upper() == "Y":

                customers.remove(customer)

                write_data(CUSTOMER_FILE, customers)

                print_success("Customer Deleted Successfully")

            else:

                print("Delete Cancelled")

            return

    print_error("Customer Not Found")
