from modules.file_handler import read_data
from utils.helper import print_header


CUSTOMER_FILE = "app/database/customers.json"
ORDER_FILE = "app/database/orders.json"
STAFF_FILE = "app/database/staff.json"
TABLE_FILE = "app/database/tables.json"
BILL_FILE = "app/database/bills.json"


# ================= TOTAL CUSTOMERS =================

def total_customers():

    print_header("CUSTOMER REPORT")

    customers = read_data(CUSTOMER_FILE)

    print("\n" + "=" * 40)
    print(f"Total Customers : {len(customers)}")
    print("=" * 40)


# ================= TOTAL ORDERS =================

def total_orders():

    print_header("ORDER REPORT")

    orders = read_data(ORDER_FILE)

    print("\n" + "=" * 40)
    print(f"Total Orders : {len(orders)}")
    print("=" * 40)


# ================= TOTAL SALES =================

def total_sales():

    print_header("SALES REPORT")

    orders = read_data(ORDER_FILE)

    total_sale = 0

    for order in orders:

        total_sale += order["total"]

    print("\n" + "=" * 40)
    print(f"Total Sales : ₹{total_sale}")
    print("=" * 40)


# ================= TOTAL STAFF =================

def total_staff():

    print_header("STAFF REPORT")

    staffs = read_data(STAFF_FILE)

    print("\n" + "=" * 40)
    print(f"Total Staff : {len(staffs)}")
    print("=" * 40)


# ================= TOTAL TABLE BOOKINGS =================

def total_tables():

    print_header("TABLE REPORT")

    tables = read_data(TABLE_FILE)

    print("\n" + "=" * 40)
    print(f"Total Booked Tables : {len(tables)}")
    print("=" * 40)


# ================= TOTAL BILLS =================

def total_bills():

    print_header("BILL REPORT")

    bills = read_data(BILL_FILE)

    print("\n" + "=" * 40)
    print(f"Total Bills : {len(bills)}")
    print("=" * 40)


# ================= PAID BILLS =================

def paid_bills():

    print_header("PAID BILL REPORT")

    bills = read_data(BILL_FILE)

    paid = 0

    for bill in bills:

        if bill["payment_status"] == "Paid":

            paid += 1

    print("\n" + "=" * 40)
    print(f"Paid Bills : {paid}")
    print("=" * 40)


# ================= TOTAL REVENUE =================

def total_revenue():

    print_header("REVENUE REPORT")

    bills = read_data(BILL_FILE)

    revenue = 0

    for bill in bills:

        if bill["payment_status"] == "Paid":

            revenue += bill["grand_total"]

    print("\n" + "=" * 40)
    print(f"Total Revenue : ₹{round(revenue,2)}")
    print("=" * 40)


# ================= MOST ORDERED ITEM =================

def most_ordered_item():

    print_header("TOP SELLING ITEM")

    orders = read_data(ORDER_FILE)

    if len(orders) == 0:

        print("No Orders Found")
        return

    items = {}

    for order in orders:

        item_name = order["item_name"]

        if item_name in items:

            items[item_name] += order["quantity"]

        else:

            items[item_name] = order["quantity"]

    max_item = ""
    max_qty = 0

    for item, qty in items.items():

        if qty > max_qty:

            max_qty = qty
            max_item = item

    print("\n" + "=" * 50)
    print(f"Top Selling Item : {max_item}")
    print(f"Total Quantity   : {max_qty}")
    print("=" * 50)


# ================= BUSINESS SUMMARY =================

def business_summary():

    print_header("RESTAURANT BUSINESS SUMMARY")

    customers = read_data(CUSTOMER_FILE)
    orders = read_data(ORDER_FILE)
    staffs = read_data(STAFF_FILE)
    tables = read_data(TABLE_FILE)
    bills = read_data(BILL_FILE)

    total_sale = 0

    for order in orders:

        total_sale += order["total"]

    revenue = 0

    for bill in bills:

        if bill["payment_status"] == "Paid":

            revenue += bill["grand_total"]

    print("\n" + "=" * 55)
    print("RESTAURANT ANALYTICS DASHBOARD")
    print("=" * 55)

    print(f"Total Customers      : {len(customers)}")
    print(f"Total Orders         : {len(orders)}")
    print(f"Total Staff          : {len(staffs)}")
    print(f"Booked Tables        : {len(tables)}")
    print(f"Total Bills          : {len(bills)}")
    print(f"Total Sales          : ₹{total_sale}")
    print(f"Total Revenue        : ₹{round(revenue,2)}")

    print("=" * 55)