# 24. Inverted pyramid
# *********
#  *******
#   *****
#    ***
#     *

number = 6
for row in range(1,number):
    for space in range(row-1):
        print(" ", end ='')

    for stars in range(number-row):
        print('A', end ='')

    for stars2 in range(number-1-row):
        print('A', end = '')

    print()