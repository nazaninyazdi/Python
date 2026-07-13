import random
c = random.randint(1,10)
while True: 
    m = int(input('Enter your number (1,10): '))
    if m==c:
        print('You win! ')
        break
    elif m<c :
        print('your number is lower than c')
        print('try again! ')
    else:
        print('your number is higher than C')
        print('try again!')