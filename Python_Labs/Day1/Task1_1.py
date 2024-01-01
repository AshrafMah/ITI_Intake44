'''Write a program that counts up the number of vowels [a, e, i, o,
u] contained in the string.'''

sentense = "Hi, my name is Ashraf. Nice to meet you"

vowels = ['a','e','i','o','u']

countVowels = 0

for char in sentense:
    if char.lower() in vowels:  #convert to case-sensitive
        countVowels += 1

print(countVowels)