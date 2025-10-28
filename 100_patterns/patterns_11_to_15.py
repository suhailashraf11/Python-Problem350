# 11. Print numbers divisible by 3 (1–30)
for i in range(1,31):
    if i % 3 == 0:
        print(f'Are the divisible number', i)

#another way to do;
for i in range(3,31, 3):
    print(i)



# 12. Print square of numbers (1–10)
for i in range(1,11):
    print(f'this is the square root {i} x {i} that is equal to {i*i}')
print('Method 2-------------------------------------------------')
for i in range(1,11):
    print(f'this is the square root {i} xx {2} that is equal to {i*2}')


# 13. Print cube of numbers (1–5)
for i in range(1,6):
    print(f'this cube {i*i*i}')

for i in range(1,6):
    print(f'this cude method two: {i**3}')


# 14. Increasing star pattern
for row in range(5):
    for col in range(row+1):
        print('*', end=' ')
    print()


print('-------------------------------------------------------------------')
for i in range(1,6):
    print('* '*i)
print('-------------------------------------------------------------------')


# 15. Decreasing star pattern
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end =' ')
    print()
print('-------------------------------------------------------------------')



