'''
Write a program that remove all vowels from the input word and
generate a brief version of it.
'''

sentense = "Hi, my name is Ashraf. Nice to meet you"

vowels = ['a','e','i','o','u']

newSentense = ""

for char in sentense: #convert to case-sensitive
    if char.lower() not in vowels:
        newSentense += char

print("Original Sentense: ",sentense)
print("Brief verion without vowels: ",newSentense)