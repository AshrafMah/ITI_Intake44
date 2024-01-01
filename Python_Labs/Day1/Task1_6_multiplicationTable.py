'''
Write a program that generate a multiplication table from 1 to the
number passed.
'''

# Take input from the user
inputNumber=int(input("Enter an number: "))

# Generate and display the multiplication table
print(f"Multiplication Table for {inputNumber}:")
for i in range(1, inputNumber+1):
    for j in range(1,i+1):
        result = i*j
        print(f"{i} x {j} = {result}")
