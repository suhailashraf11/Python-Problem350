# 24. Check whether a number is Armstrong number


n = 153
t = 0
l = len(str(n))
# print(l)

temp   = 0
calculations = []
step = []
for i in str(n):
    temp = temp + int(i) ** l
    step.append(temp + int(i) ** l)
    calculations.append(temp)
if temp == n:
    print(f'Yes, This is Armstrong Number {temp}:'
          f' \nHere the calculations { calculations}')