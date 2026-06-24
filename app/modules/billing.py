from modules.file_handler import read_data, write_data
from utils.helper import print_header, print_success, print_error


BILL_FILE = "app/database/bills.json"
ORDER_FILE = "app/database/orders.json"



# ================= GENERATE BILL =================


def generate_bill():

    print_header("GENERATE BILL")


    bills = read_data(BILL_FILE)
    orders = read_data(ORDER_FILE)


    if not isinstance(bills,list):
        bills=[]



    try:

        order_id=int(input("Enter Order ID : "))

    except ValueError:

        print_error("Invalid Order ID")
        return




    for order in orders:


        if order["order_id"] == order_id:



            for bill in bills:

                if bill["order_id"] == order_id:

                    print_error("Bill Already Generated")

                    return





            amount = order["total"]



            discount = 0


            if amount >= 1000:

                discount = amount * 0.10




            after_discount = amount - discount



            gst = after_discount * 0.18



            final_amount = after_discount + gst






            bill = {


                "order_id":order["order_id"],


                "customer_name":order["customer_name"],


                "table_no":order["table_no"],


                "category":order["category"],


                "item_name":order["item_name"],


                "type":order.get("type","Full"),


                "quantity":order["quantity"],


                "amount":amount,


                "discount":discount,


                "gst":gst,


                "final_amount":final_amount,


                "payment_mode":"Not Selected",


                "payment_status":"Pending"

            }




            bills.append(bill)


            write_data(BILL_FILE,bills)



            print_success("Bill Generated Successfully")


            show_bill(bill)


            return





    print_error("Order Not Found")






# ================= SHOW BILL =================



def show_bill(bill):


    print("\n")


    print("="*60)

    print("ALVI ROYAL RESTAURANT BILL".center(60))

    print("="*60)



    print("Order ID     :",bill["order_id"])


    print("Customer     :",bill["customer_name"])


    print("Table        :",bill["table_no"])


    print("Category     :",bill["category"])


    print("Item         :",bill["item_name"])


    print("Type         :",bill["type"])


    print("Quantity     :",bill["quantity"])


    print("-"*60)



    print("Amount       : ₹",bill["amount"])


    print("Discount     : ₹",round(bill["discount"],2))


    print("GST 18%      : ₹",round(bill["gst"],2))


    print("Final Amount : ₹",round(bill["final_amount"],2))


    print("-"*60)


    print("Payment      :",bill["payment_status"])


    print("="*60)









# ================= VIEW BILLS =================



def view_bills():


    print_header("ALL BILL HISTORY")


    bills = read_data(BILL_FILE)



    if not bills:

        print_error("No Bills Found")

        return




    for bill in bills:

        show_bill(bill)










# ================= PAYMENT =================



def payment():


    print_header("PAYMENT SYSTEM")


    bills = read_data(BILL_FILE)



    try:

        order_id=int(input("Enter Order ID : "))


    except ValueError:


        print_error("Invalid ID")

        return






    for bill in bills:



        if bill["order_id"] == order_id:




            if bill["payment_status"]=="Paid":


                print_error("Payment Already Done")

                return




            print("\nPayment Mode")

            print("1. Cash")

            print("2. Card")

            print("3. UPI")



            choice=input("Select : ")





            if choice=="1":

                bill["payment_mode"]="Cash"



            elif choice=="2":

                bill["payment_mode"]="Card"



            elif choice=="3":

                bill["payment_mode"]="UPI"



            else:

                print_error("Invalid Choice")

                return






            bill["payment_status"]="Paid"



            write_data(BILL_FILE,bills)



            print_success("Payment Successful")


            print("Paid Amount ₹",round(bill["final_amount"],2))


            return





    print_error("Bill Not Found")









# ================= HISTORY =================


def bill_history():

    view_bills()