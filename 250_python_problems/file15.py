# 15. Swap two numbers without using a third variable
# Method 1 usinf arthmetic operations


a = int(input('enter a :'))

b = int(input('enter b :'))
n , m = a, b
a  =  a+b
b = a -b
a = a-b

print(f'{n} ={a}  = {m}= {b}')
# 5 + 10 =15  dry run
# 15 - 10 = 5 dry run
# 15 - 5 = 10 dry run


c ,d = 100, 200
print(c,d)
c = c ^ d
d = c ^ d
c = c ^ d

print(c,d)


m,n = 300 , 500

m,n = n,m
print(m,n)