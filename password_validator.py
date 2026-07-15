def check_password(password):
    return (
        check_len(password)
        and include_number(password)
        and include_upper(password)
        and include_lower(password)
    )


def check_len(password):
    return len(password) >= 8


def include_number(password):
    numbers = "0123456789"
    for char in password:
        if char in numbers:
            return True
    return False


def include_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False


def include_lower(password):
    for char in password:
        if char.islower():
            return True
    return False


print(check_password("Na12345678"))
