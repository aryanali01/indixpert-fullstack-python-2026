# ================= VALIDATION FUNCTIONS =================

def validate_password(password):
    """
    Password must be at least 6 characters
    """
    if len(password) >= 6:
        return True

    return False


def validate_username(username):
    """
    Username must be at least 3 characters
    """
    if len(username.strip()) >= 3:
        return True

    return False


def validate_name(name):
    """
    Name should not be empty
    """
    if len(name.strip()) >= 2:
        return True

    return False


def validate_address(address):
    """
    Address should not be empty
    """
    if len(address.strip()) > 0:
        return True

    return False


def validate_qualification(qualification):
    """
    Qualification should not be empty
    """
    if len(qualification.strip()) > 0:
        return True

    return False


def validate_empty(value):
    """
    Generic Empty Validation
    """
    if value.strip() != "":
        return True

    return False