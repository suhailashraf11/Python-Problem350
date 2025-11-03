# 30. Right aligned triangle
#     *
#    **
#   ***
#  ****
# *****


n = 6
for row in range(1,n):
    for space_col in range(n-row):
        print(" ", end =' ')
    for stars in range(row):
        print("*", end =' ')
    print()
