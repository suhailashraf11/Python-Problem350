# 20. Calculate power of a number using loop



base = int(input('enter number: '))
expo = int(input('enter the number: '))
if base == 0:
    print('Enter number above ',base)
elif base == 1:
    print('Number is ',  base)

for i in range(1,expo+1):
    power = base * i

    print(power)
print(base)



