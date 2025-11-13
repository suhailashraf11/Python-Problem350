# 36. Hollow right triangle
# *
# * *
# *   *
# *     *
# *******




n = 6
for row in range(1,n):
    if row == 5:
        print("*"*5)
    elif row ==1:
        print('*'*row)
    else:
        space = 2 * row -3
        empty = ' '
        print('*',empty *space ,'*' )

