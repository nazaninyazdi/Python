import random
mw = 0 #me win
cw = 0 #computer win
be = 0 #both equal
n = int(input('Enter your numbers of playing: '))
i = 1
while True:
    m = input('Enter your choice: ')
    possible_actions = ['rock', 'paper', 'scissors']
    c = random.choice(possible_actions)
    if m==c:
        print('Tie!')
        be = be+1
    elif m=='rock':
        if c=='scissors':
            print('You won!')
            print(c)
            mw = mw+1
        else:
            print('Computer won!')
            print(c)
            cw = cw+1
    elif m=='paper':
        if c=='rock':
            print('You won!')
            print(c)
            mw = mw+1
        else:
            print('Computer won!')
            print(c)
            cw = cw+1
    elif m=='scissors':
        if c=='paper':
            print('You won!')
            print(c)
            mw = mw+1
        else:
            print('Computer won!')
            print(c)
            cw = cw+1
    i = i+1
    if i>n:
        break 
print('number of you win is %s'%mw)
print('numbers of computer win is %s'%cw)
print('number of equalities is %s'%be)
