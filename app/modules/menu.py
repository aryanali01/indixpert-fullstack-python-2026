from modules.file_handler import read_data, write_data
from utils.helper import print_header, print_success, print_error


MENU_FILE = "app/database/menu.json"


CATEGORIES = [
    "Breakfast",
    "Lunch",
    "Dinner",
    "Fast Food",
    "Chinese",
    "South Indian",
    "Soft Drinks",
    "Mocktails",
    "Ice Cream",
    "Desserts",
    "Beverages"
]



# ================= FIX MENU FORMAT =================

def fix_menu(menu):

    if isinstance(menu, list):

        new_menu = {}

        for c in CATEGORIES:
            new_menu[c] = []

        return new_menu


    return menu




# ================= ADD ITEM =================


def add_item():


    print_header("ADD RESTAURANT MENU ITEM")


    menu = fix_menu(read_data(MENU_FILE))



    try:

        item_id = int(input("Enter Item ID : "))

    except:

        print_error("ID Must Be Number")
        return





    for category,items in menu.items():

        for item in items:


            if item["id"] == item_id:

                print_error("Item Already Exists")

                return






    print("\n===== CATEGORY =====")


    for i,c in enumerate(CATEGORIES,1):

        print(f"{i}. {c}")



    try:

        choice=int(input("Select Category : "))


        category=CATEGORIES[choice-1]


    except:

        print_error("Invalid Category")

        return






    name=input("Enter Food Name : ")


    food_type=input("Veg / Non-Veg : ")





    try:

        half=float(input("Half Price : ₹"))


        full=float(input("Full Price : ₹"))


    except:

        print_error("Invalid Price")

        return







    item={


        "id":item_id,

        "name":name,

        "food_type":food_type,

        "half_price":half,

        "full_price":full

    }





    menu[category].append(item)



    write_data(MENU_FILE,menu)



    print_success("Item Added Successfully")








# ================= VIEW =================


def view_items():


    print_header("RESTAURANT MENU")


    menu=fix_menu(read_data(MENU_FILE))



    for category,items in menu.items():


        print("\n"+"="*55)

        print(category.center(55))

        print("="*55)



        if not items:

            print("No Items")



        for item in items:



            print("ID          :",item["id"])


            print("Name        :",item["name"])


            print("Type        :",item["food_type"])


            print("Half Price  : ₹",item["half_price"])


            print("Full Price  : ₹",item["full_price"])


            print("-"*55)








# ================= SEARCH =================


def search_item():


    print_header("SEARCH ITEM")


    menu=fix_menu(read_data(MENU_FILE))


    name=input("Enter Food Name : ")




    for category,items in menu.items():


        for item in items:



            if item["name"].lower()==name.lower():



                print("\nITEM FOUND")


                print("Category :",category)


                print("Name :",item["name"])


                print("Half : ₹",item["half_price"]
                )


                print("Full : ₹",item["full_price"])


                return




    print_error("Item Not Found")






# ================= UPDATE =================


def update_item():


    print_header("UPDATE ITEM")


    menu=fix_menu(read_data(MENU_FILE))



    try:

        item_id=int(input("Enter Item ID : "))

    except:

        print_error("Invalid ID")

        return






    for category,items in menu.items():


        for item in items:



            if item["id"]==item_id:



                item["name"]=input("New Name : ")



                item["food_type"]=input("New Type : ")



                item["half_price"]=float(input("New Half Price : "))



                item["full_price"]=float(input("New Full Price : "))



                write_data(MENU_FILE,menu)



                print_success("Updated Successfully")


                return





    print_error("Item Not Found")









# ================= DELETE =================


def delete_item():


    print_header("DELETE ITEM")


    menu=fix_menu(read_data(MENU_FILE))


    try:

        item_id=int(input("Enter Item ID : "))

    except:

        print_error("Invalid ID")

        return






    for category,items in menu.items():


        for item in items:



            if item["id"]==item_id:



                items.remove(item)



                write_data(MENU_FILE,menu)


                print_success("Deleted Successfully")


                return





    print_error("Item Not Found")