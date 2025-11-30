# 23. Find GCD of two numbers


num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))
print(num1,num2 )

if num2 > num1:
    mini = num1
else:
    mini = num2
for i in range(1, mini+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        print(f'The GCD {gcd}, and this is this is the actully count {i}')
print('The final GCD IS : ', gcd)

