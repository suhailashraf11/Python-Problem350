# 37. Half diamond pattern
# *
# **
# ***
# ****
# ***
# **
# *

n = 6
# for i in range(1,n):
#     for j in range(i):
#         print('*', end = '')
#     print()
# for i in range(n-2,0,-1):
#     for j in range(i):
#         print('*', end= '')
#     print()


for i in range(1, n+1):
    print('* '* i)
for j in range(n-1,0 ,-1):
    print('* '*j)
