# 34. Reverse number triangle
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for row in range(5,0,-1):
    for col in range(row,0, -1):
        print(col, end =' ')
    print()



