"""

"""
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
egyptian_number_regex = r'^\+20\d{10}$'


def checkName(fname,lname):
    while True:
        if not (fname.isalpha() and lname.isalpha()):
            print("Invalid name")
            fname = input("Enter your first name again: ")
            lname = input("Enter your last name again: ")
        else:
            return fname, lname
            break


def checkEmail(email):
    while True:
        if not re.match(regex,email):
            print("Invalid Email")
            email = input("Enter your Email again: ")
        else:
            return email
            break

def checkPassword(password,confirmPassword):
    while True:
        if password != confirmPassword:
            print("Passwords do not match")
            confirmPassword =input("Confirm password:")
        else:
            return password
            break

def checkEgyNumber(mobileNumber):
    while True:
        if not re.match(egyptian_number_regex, mobileNumber):
            print("Invalid Number")
            mobileNumber = input("Enter a valid Egyptian phone number: ")
        else:
            return mobileNumber
            break


