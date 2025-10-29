# 6. Calculate the sum of first N natural numbers
nums = 0
n = int(input('enter the number: '))
for i in range(n+1):
    nums = nums + i
    # print(i, nums) # dry run
print(nums)


# 7. Reverse a given number

number  = 13456
nums = 1

# 8. Find factorial of a number using loop
factors = int(input('enter the number: '))
initial = 0
for i in range(1,factors+1):
    initial *=  i
print('this is initial', initial)

# 9. Calculate simple interest and compound interest
p , r , t = int(input('enter the p:')),int(input('enter the r :')),int(input('enter the t :'))
const = 100
ask = input('What are you looking for Simple Intrest type [SI] or for compound intrest type [CI]: ').lower()
if ask == 'si':
    simple_intrest  = (p * r * t )/const
    print(f'this your simple intrest = {simple_intrest}')
elif ask == 'ci':
    compounding_intrest = p*(1 + int(r)/int(const))**t-p
    print(f'This is compound intrest = {compounding_intrest}')
else:
    print('Invalid values')

# 10. Check if a number is prime
check = int(input('enter the number: '))
if check % 2 == 0:
    print(check, 'prime')
else:
    print(check, 'odd')