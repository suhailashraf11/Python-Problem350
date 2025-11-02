# 27. Hollow square (5×5)
# *****
# *   *
# *   *
# *   *
# *****

n =6
for row in range(1, n):
    for col in range(1, n):
        # if row >=2 and row<=4 and col >=2 and col <=4:
        '''
        About logic is correct but too long
        blow is used for more reliable result and simple code readablity.
        
        '''
        if 2 <= row <= 4 and 2 <= col <= 4:

            print(' ', end = ' ')

        else:
            print("#", end =' ')

    print()





