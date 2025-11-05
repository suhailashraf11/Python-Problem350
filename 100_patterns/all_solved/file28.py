# 28. Hollow triangle
# *
# * *
# *   *
# *****

n = 6

for  row in range(n-1,0,-1):
    if row ==1:
        print('*')
    elif row == 5:
        print('*'*5)
    else:
        space = 2 * row - 3
        print("*", '_' *space , '*')



