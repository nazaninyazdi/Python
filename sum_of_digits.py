def sum_digits(num):
    if num < 0:
        num = - num

    total = 0

    while num != 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


print(sum_digits(62))
print(sum_digits(-71))