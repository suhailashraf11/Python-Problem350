n  = 5 #int(input('enter the number :'))
for i in range(1, n+1):
    print(' ' * (n-i) + "*" *i)

# method 2

for row in range(1, n+1):
    for space in range(n - row):
        print(' ', end = ' ')
    for stars in range(row):
        print('*', end = ' ')
    print()

