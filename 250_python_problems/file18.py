# 18. Check if a string is palindrome
name  = input('enter the something to check wheater it is palindrom or not: ')
name_reverse  = name[::-1]

print(name, name_reverse)
if name_reverse == name:
    print(f'Yes this is palindrome {name}')
else:
    print(f'No this is not a palindrome {name_reverse}')
