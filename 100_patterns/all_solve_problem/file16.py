# 16. Number repeated per row

for i in range(1,6):
    for j in range(i ):
        print(i, end = ' ')
    print()


for i in range(1,6):
    print(str(i) * i)



# 17. Number triangle (1 to n)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end  = ' ')
    print()

# 18. Alphabet triangle (A to D)
# A
# A B
# A B C
# A B C D
for i in range(ord('A'), ord('E')):
    for j in range(ord('A'), i +1):
        print(chr(j), end =' ')
    print()



# 19. Diagonal star pattern
# *0000
# 0*000
# 00*00
# 000*0
# 0000*

for i in range(1,6):
    for j in range(1, 6):
        if i == j:
            print('*' , end = ' ')
        else:
            print('O', end = ' ')
    print()
#20. Number square (same number in row)
# 11111
# 22222
# 33333
# 44444
# 55555
for i in range(1,6):
    for j in range(1,6):
        print(i, end = ' ')
    print()




