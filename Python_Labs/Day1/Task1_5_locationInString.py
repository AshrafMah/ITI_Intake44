'''
Write a program that prints the locations of "i" character in any
string you added.
'''

sentense = "Hi, my name is Ashraf. Nice to meet you"
searchChar='i'
location =[]

for index,char in enumerate(sentense):
    if char.lower() == searchChar:
        location.append(index)

print(f'location of {searchChar}: ', location)