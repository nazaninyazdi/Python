def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
def describe_number(num):
    if num == 0:
        return "Zero"
    elif num > 0:
        if is_even(num):
            return "Positive even"
        else:
            return "Positive odd"
    else:
        if is_even(num):
            return "Negative even"
        else:
            return "Negative odd"
        
print(describe_number(0))
print(describe_number(7))
print(describe_number(8))
print(describe_number(-7))
print(describe_number(-8))