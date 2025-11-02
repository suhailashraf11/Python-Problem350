# 23. Full pyramid
#     *
#    ***
#   *****
#  *******
# *********
nums = 6

for row in range(1,nums):
    for space in range(nums -row):
        print(" ", end = '')
    for stars in range(row):
        print("A", end = '')
    for stars2 in range(row-1):
        print("A", end='')
    print()




