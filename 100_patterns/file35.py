n =6

for  row in range(1, n):
    for space in range(n-row-1):
        print(' ',end='')
    for stars in range(row):
        print("*", end= '')
    print()
