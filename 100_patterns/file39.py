# 39. Alternating 1s and 0s
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

n = 6
for i in range(1,n):
    for j in range(i):
        if j % 2 == 0 and i % 2 == 0  :
            print(0, end ='')
        else:
            print(1, end= '')

    print()


