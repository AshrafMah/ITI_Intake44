'''
Write a function which has an input of a string from user then it
will return the same string reversed.
'''


def reverseString(inputStr):
    return inputStr[::-1]


data = str(input('Enter your string: '))
reversedString = reverseString(data)
print(reversedString)
