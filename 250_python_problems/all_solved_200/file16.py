# 16. Convert Celsius to Fahrenheit


temperature = int(input('Enter the numbers :'))


unit = input('enter the unit like c or f : ').lower()

if unit =='f':
    #bodman
    result_f = temperature * (9/5) + 2
    print(result_f)
elif unit =='c':
    # bodmas
    result_c = temperature -32*(5/9)
    print(result_c)
else:
    print('enter the correct values')


# working correctly there something technical issue that needs to be fixed , i am in hurry wait.

