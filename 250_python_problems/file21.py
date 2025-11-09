#. Calculate power of a number using loop    (Not solved)


num = int(input('enter the number: '))
power = int(input('enter the power: '))
total = 1
for i in range(1,power+1):
    total = total * num
    print(total,i)
print(f'This is the finally result after all the executions : {total}')
