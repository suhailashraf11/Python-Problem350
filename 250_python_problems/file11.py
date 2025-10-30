# 11. Generate multiplication table of a number

nums  = int(input("enter the number: "))

for i in range(1,11):
    print(f'{nums} x {i} = {nums*i}')