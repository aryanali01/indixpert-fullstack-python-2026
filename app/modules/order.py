from modules.file_handler import read_data, write_data
from utils.helper import print_header, print_success, print_error


ORDER_FILE = "app/database/orders.json"
MENU_FILE = "app/database/menu.json"



# ================= PLACE ORDER =================


def place_order():


    print_header("PLACE NEW ORDER")


    orders = read_data(ORDER_FILE)
    menu = read_data(MENU_FILE)



    try:

        order_id = int(
            input("Enter Order ID : ")
        )

        table_no = int(
            input("Enter Table Number : ")
        )

        item_id = int(
            input("Enter Item ID : ")
        )

        quantity = int(
            input("Enter Quantity : ")
        )


    except ValueError:

        print_error(
            "Only Number Allowed"
        )

        return




    customer_name = input(
        "Enter Customer Name : "
    )





    for order in orders:


        if order["order_id"] == order_id:


            print_error(
                "Order ID Already Exists"
            )

            return






    selected_item = None
    category_name = ""




    for category,items in menu.items():


        for item in items:



            if item["id"] == item_id:


                selected_item = item
                category_name = category

                break



        if selected_item:

            break







    if selected_item is None:


        print_error(
            "Item Not Found"
        )

        return








    print("\n===== SELECT TYPE =====")

    print("1. Half")
    print("2. Full")



    choice=input(
        "Enter Choice : "
    )





    if choice=="1":


        order_type="Half"

        price = selected_item["half_price"]




    elif choice=="2":


        order_type="Full"

        price = selected_item["full_price"]




    else:


        print_error(
            "Invalid Type"
        )

        return





    total = price * quantity







    order = {


        "order_id":
        order_id,


        "customer_name":
        customer_name,


        "table_no":
        table_no,



        "category":
        category_name,



        "item_id":
        item_id,



        "item_name":
        selected_item["name"],



        "food_type":
        selected_item.get(
            "food_type",
            "Veg"
        ),



        "type":
        order_type,



        "quantity":
        quantity,



        "price":
        price,



        "total":
        total,



        "status":
        "Pending"

    }







    orders.append(order)



    write_data(
        ORDER_FILE,
        orders
    )




    print_success(
        "Order Placed Successfully"
    )



    print("\n========== ORDER SUMMARY ==========")


    print(
        "Category :",
        category_name
    )


    print(
        "Item :",
        selected_item["name"]
    )


    print(
        "Type :",
        order_type
    )


    print(
        "Price : ₹",
        price
    )


    print(
        "Quantity :",
        quantity
    )


    print(
        "Total : ₹",
        total
    )


    print(
        "=================================="
    )









# ================= VIEW ORDERS =================


def view_orders():


    print_header(
        "ORDER HISTORY"
    )


    orders = read_data(
        ORDER_FILE
    )



    if not orders:


        print_error(
            "No Orders Found"
        )

        return






    for order in orders:



        print("\n"+"="*55)


        print(
            "RESTAURANT ORDER".center(55)
        )


        print("="*55)




        print(
            "Order ID :",
            order["order_id"]
        )


        print(
            "Customer :",
            order["customer_name"]
        )


        print(
            "Table :",
            order["table_no"]
        )


        print(
            "Category :",
            order["category"]
        )


        print(
            "Item :",
            order["item_name"]
        )


        print(
            "Type :",
            order["type"]
        )


        print(
            "Quantity :",
            order["quantity"]
        )


        print(
            "Price : ₹",
            order["price"]
        )


        print(
            "Total : ₹",
            order["total"]
        )


        print(
            "Status :",
            order["status"]
        )


        print("="*55)









# ================= UPDATE ORDER =================


def update_order():


    print_header(
        "UPDATE ORDER"
    )



    orders = read_data(
        ORDER_FILE
    )



    try:

        order_id=int(
            input("Enter Order ID : ")
        )


    except:


        print_error(
            "Invalid ID"
        )

        return






    for order in orders:



        if order["order_id"] == order_id:



            try:

                qty=int(
                    input("New Quantity : ")
                )


            except:


                print_error(
                    "Invalid Quantity"
                )

                return






            order["quantity"] = qty



            order["total"] = (
                qty *
                order["price"]
            )





            write_data(
                ORDER_FILE,
                orders
            )



            print_success(
                "Order Updated Successfully"
            )


            return





    print_error(
        "Order Not Found"
    )










# ================= CANCEL ORDER =================


def cancel_order():


    print_header(
        "CANCEL ORDER"
    )


    orders = read_data(
        ORDER_FILE
    )



    try:

        order_id=int(
            input("Enter Order ID : ")
        )


    except:


        print_error(
            "Invalid ID"
        )

        return






    for order in orders:



        if order["order_id"] == order_id:



            orders.remove(order)



            write_data(
                ORDER_FILE,
                orders
            )


            print_success(
                "Order Cancelled Successfully"
            )


            return





    print_error(
        "Order Not Found"
    )