# 41. Full diamond pattern
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
#
n = 5
# for i in range(1, n):
#     for j in range(n-i):
#         print(' ', end = '')
#
#     for k in range(i):
#         print('*', end ='')
#
#     for l in range(1,i):
#         print('*', end ='')
#     print()
#
# for a in range(2,n):
#     for b in range(a):
#         print(' ', end ='')
#     for c in range(n-a):
#         print('*', end = '')
#
#     print()
#     for d in range(n-a-1):
#         print('*', end ='')


#
# Top half (including middle row)
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))

# Bottom half
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))

