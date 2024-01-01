'''
Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in
alphabetical order is: abdu
'''



def longestOrder(inputStr):
    currentSubstring = inputStr[0]
    longestSubstring = inputStr[0]

    for char in inputStr[1:]:
        if char >= currentSubstring[-1]:
            currentSubstring += char
        else:
            currentSubstring = char
        if len(currentSubstring) > len(longestSubstring):
            longestSubstring = currentSubstring

    return longestSubstring


data = str(input("Enter your string: "))

result = longestOrder(data)

print(f"Longest substring in alphabetical order is: {result}")
