'''
Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start.
'''

def generateArray(length, start):
    generatedArray = [start +i for i in range(length)]
    return generatedArray

arrayLength = int(input("Enter array length: "))
arrayStart = int(input("Enter array start: "))

array = generateArray(arrayLength, arrayStart)
print(array)
