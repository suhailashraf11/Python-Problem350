# 31. Number triangle (1 to n)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


n = int(input('enter number for better result  take atleast 6 or 5 digits above values: '))
for row in range(1, n):
    for col in range(1,row+1):
        print(col, end= ' ')
    print()
