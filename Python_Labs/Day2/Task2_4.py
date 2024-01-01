'''
Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not
'''

import re

name = input('Enter your Name: ')

while not name.strip() or any(char.isdigit() for char in name):
    if not name.strip():
        print("Please enter a valid Name.")
    elif any(char.isdigit() for char in name):
        print("Name shoudn't contain numbers")
    name = input('Enter your Name: ')

email = input('Enter your Email: ')


def isEmailValid(email):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.match(pattern, email)


while not isEmailValid(email):
    print("Please enter a valid email")
    email = input('Enter your Email: ')

print('Name: ', name)
print('Email', email)
