#write a program to print give password is valid or not
#password should contain at least 1 upper,lower,symbol and digit
n=input()
li=list(n)
u=0
l=0
s=0
d=0
for i in li:
    if i is upper:
        u=u+1
    elif i is lower:
        l=l+1
    elif i is symbol:
        s=s+1
    elif i is digit:
        d=d+1
if u>o and l>0 and s>o and d>0:
    print('password is valid')
else:
    print('password is not valid')
