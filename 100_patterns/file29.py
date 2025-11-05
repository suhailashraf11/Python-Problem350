# #29. Hollow inverted triangle
# *****
# *   *
# * *
# *


nums = 5
for row in range(nums,0,-1):
    if row == 5:
        print('*'*row)
    elif row == 1:
        print('*'*row)

    else:
        space = 2 *  row -3
        print('*',' '* space,'*')
