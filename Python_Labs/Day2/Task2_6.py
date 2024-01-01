'''
Write a program which repeatedly reads numbers until the user
enters “done”.
○ Once “done” is entered, print out the total, count, and
average of the numbers.
○ If the user enters anything other than a number, detect their
mistake, print an error message and skip to the next number.
'''

numbers = []

while True:
    data = input("Enter a number (type 'done' to finish): ")

    if data.lower() == 'done':
        break  # Exit the loop if the user enters 'done'

    try:
        number = int(data)  # Convert the input to int
        numbers.append(number)

    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Display the entered numbers
print("Entered numbers:", numbers)
print("Sum= ", sum(numbers))
print("count= ", len(numbers))
if len(numbers) > 0:
    print("Average= ", sum(numbers)/len(numbers))
else:
    print("numerator divided by zero!!")
