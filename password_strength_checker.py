def password_strength(password):
    
    count = 0
     
    if not check_len(password):
        print("Length: ✘")
        return "Very weak"    
    print("Length: ✔")
    if include_number(password):
        count+=1
        print("Number: ✔")
    else:
        print("Number: ✘")
    if include_lower(password):
        count+=1
        print("Lower: ✔")
    else:
        print("Lower: ✘")
    if include_upper (password):
        count+=1
        print("Upper: ✔")
    else:
        print("Upper: ✘")
    if include_special(password):
        count+=1
        print("Special: ✔")
    else:
        print("Special: ✘")
    

    if count == 4:
        return "Very strong password"
    elif count == 3:
        return "Strong password"
    elif 2 == count :
        return "Medium"
    elif count == 1:
        return "Weak"
    elif count == 0:
        return "Very weak"


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

def include_special(password):
    special = "!@#$%^&*()_+-=?.,"
    for char in password:
        if char in special:
            return True
    return False

def main():
    password = input("Enter your password: ")
    print(password_strength(password))
main()

