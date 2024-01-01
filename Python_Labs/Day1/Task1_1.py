sentense = "Hellooo this is change branch.Welcome in my new branch"

vowels = ['a','e','i','o','u']

countVowels = 0

for char in sentense:
    if char.lower() in vowels:  #convert to case-sensitive
        countVowels += 1

print(countVowels)