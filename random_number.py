import random 
n = int(input('Enter your number: '))
numbers = list(range(1, n+1))
random.shuffle(numbers)
for i, num in enumerate(numbers, start=1):
    print(f"{i} : {num}")


