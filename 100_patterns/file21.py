n = int(input('enter the number: '))

# for i in range(n):
#     print(i*'* ')

for row in range(n):
    for col in  range(row):
        print("*", end = ' ')

    print()