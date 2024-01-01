import re

# In-memory storage for user data
users = []


def validate_phone_number(phone):
    # Basic validation for Egyptian phone numbers (11 digits starting with 01)
    return re.match(r'^01[0-9]{9}$', phone)


def register():
    print("Registration:")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")

    # Check if email is already registered
    if any(user['email'] == email for user in users):
        print("Email is already registered. Please choose a different email.")
        return

    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match. Registration failed.")
        return

    mobile_phone = input("Enter Mobile Phone: ")

    if not validate_phone_number(mobile_phone):
        print("Invalid phone number. Please enter a valid Egyptian phone number.")
        return

    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'mobile_phone': mobile_phone,
        'activated': False  # User is not activated initially
    }

    users.append(user_data)
    print("Registration successful. Please wait for activation.")


def login():
    print("Login:")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    # Find user with given email and password
    user = next((user for user in users if user['email'] == email and user['password'] == password), None)

    if user:
        if user['activated']:
            print("Login successful. Welcome, {} {}!".format(user['first_name'], user['last_name']))
        else:
            print("Account not activated yet. Please wait for activation.")
    else:
        print("Invalid email or password. Login failed.")


# Example usage
register()
login()
