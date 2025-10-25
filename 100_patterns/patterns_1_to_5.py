# 1. Print 5 stars in one line
# 2. Print 10 numbers (1–10) in one line
# 3. Print 1 to 10 vertically
# 4. Print 5 stars vertically
# 5. Print characters A–E


for i in range(5):
    print("*", end = ' ')

print()
# ---------------------------------------------
for i in range(1,11):
    print(i , end = ' ')
# ---------------------------------------------
for i in range(1,11):
    print("*")
# ---------------------------------------------
for i in range(1,6):
    print(i)
# ---------------------------------------------
for i in range(ord('A'), ord('E') +1):
    print(chr(i) , end = ' ')
print()
# ---------------------------------------------