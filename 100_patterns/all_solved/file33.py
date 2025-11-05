n = int(input('enter the number: '))
for i in range(1, n+1):
    for j in  range(n-i):
        print(' ', end = '')

    for s in range(i):
        print('*', end  = '')
    print()

# Solved