# 25. Diamond half pattern
#
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
nums =6
for row in range(1,nums):
    for stars in range(row):
        print('*',end = '')
    print()
for row in range(nums):
    for stars in range(nums-row):
        print('*', end = '')
    print()

