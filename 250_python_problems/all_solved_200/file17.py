# 17. Check if a character is a vowel or consonant

def greet(n):
    return 'Hello ' + n +' How are you welcome to find answers!'

name  = input('enter your name: ')
print(greet(name))


alpha = input('enter the laters').lower()
vowel = ['a','e', 'i', 'o', 'u']
if  alpha in vowel:
    print(f'Yes,This letter is vowels {alpha}')
else:

    print(f'No,This letter is consonants {alpha}')

