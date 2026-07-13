num = int(input("Enter your number: "))
a = num-1
s = 0 
while a>=1:
    r = num % a 
    if r==0:
        s=s+a
    a = a-1
if num==s:
    print('True')
else:
    print('False')