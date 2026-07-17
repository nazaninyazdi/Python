def length_of_number(number):
    count = 0

    if number == 0:
        return 1
    
    while number != 0:
        number = number // 10
        count += 1

    return count

print(length_of_number(99))