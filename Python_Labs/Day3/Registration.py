"""
1-Authentication System:
  a-Registration:
    •First name
    •Last name
    •Email
    •Password
    •Confirm password
    •Mobile phone [validated against Egyptian phone numbers]
"""

import uuid
from CheckPoint import checkName, checkEmail, checkPassword, checkEgyNumber

users = []

# Define register function
def register():
    print("Registration:")
    userId = uuid.uuid4()
    fName = input("First Name: ")
    lName =input("Last Name: ")
    checkName(fName,lName)
    email = checkEmail(input("Email: "))
    password = input("Password: ")
    confirmPassword = input("Confirm Password: ")
    checkPassword(password,confirmPassword)
    mobileNumber = checkEgyNumber(input("Mobile Number: "))

    userInfo = {
        "ID":userId,
        "First Name":fName,
        "Last Name":lName,
        "Email":email,
        "Password":password,
        "Mobile Number":mobileNumber
    }
    users.append(userInfo)
    return users
#register()