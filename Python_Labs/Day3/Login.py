"""
b-Login
    •The user should be able to login after activation using his email and password
"""

from Registration import register

def login(users):
    print("Login:")
    while True:
        email = input("Email: ")
        password = input("Password: ")
        if any(user['Email'] == email for user in users):
            user = next(user for user in users if user['Email'] == email)
            if password == user['Password']:
                print("Login successful!")
                return user['Email']
            else:
                print("Incorrect password, Please try again.")
        else:
            print("Email not found. Please check your email or register if you don't have an account.")
            return None

registered_user = register()
login(registered_user)

