# 38. Reverse half diamond pattern
# ****
# ***
# **
# *
# **
# ***
# ****


n = 6
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print('*', end  ='')
#     print()
#
# for i in range(2,n):
#     for j in range(i):
#         print('*', end ='')
#     print()
#

for i in range(n-1, 0,-1):
    print('*' * i)

for i in range(2, n):
    print('*'*i)
