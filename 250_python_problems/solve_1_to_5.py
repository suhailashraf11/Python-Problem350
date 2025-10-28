# 1. Print 'Hello, World!'
print('hello world')
# 2. Add two numbers entered by the user
x,y = int(input('enter number')), int(input('enter number'))
sums = x+y
print(sums)


# 3. Find the largest of three numbers
nums  = [12,2,111]
largest  = max(nums)
print(largest)

m = 0
for i in range(len(nums)):
    if nums[i] > m:
        m = nums[i]
print(m)
# 4. Check whether a number is even or odd

for i in range(1,11):
    if i % 2 == 0:
        print(i , 'even')
    else:
        print(i,'_odd')

# 5. Check whether a year is a leap year
year = int(input('enter the year'))
if year % 4 == 0 and year  % 100 == 0 and year % 400== 0:
    print('leap year', year)
else:
    print('Not a leap year', year)