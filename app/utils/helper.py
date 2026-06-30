# ================= USER ID GENERATOR =================

def generate_user_id(users):

    if len(users) == 0:
        return 1

    return users[-1]["id"] + 1


# ================= HEADER DESIGN =================

def print_header(title):

    print("\n")
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


# ================= SUCCESS MESSAGE =================

def print_success(message):

    print(f"\n[SUCCESS] {message}")


# ================= ERROR MESSAGE =================

def print_error(message):

    print(f"\n[ERROR] {message}")


# ================= INFO MESSAGE =================

def print_info(message):

    print(f"\n[INFO] {message}")


# ================= LINE DESIGN =================

def print_line():

    print("-" * 60)


# ================= DASHBOARD CARD =================

def print_card(title):

    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)