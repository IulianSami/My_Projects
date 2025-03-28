#7.  🔑🔐  Alegere parola random (cel putin :2 litere mici, 2 litere mari, 2 simboluri, 2 numere) si cu verificare complexitate:

import random
import string

# Defining character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = "!@#$%^&*()_-+=?><[]"

all_chars = lower + upper + numbers + symbols

# Function to check password complexity
def check_password_complexity(password):
    has_lower = sum(1 for char in password if char in lower) >= 2
    has_upper = sum(1 for char in password if char in upper) >= 2
    has_number = sum(1 for char in password if char in numbers) >= 2
    has_symbol = sum(1 for char in password if char in symbols) >= 2

    if has_lower and has_upper and has_number and has_symbol:
        return True
    else:
        return False

# Generating the password
length = int(input("Please enter password length: "))

# Ensure the generated password has enough characters to meet the requirements
while length < 8:  # Minimum 8 characters to satisfy complexity rules
    print("The password must be at least 8 characters long.")
    length = int(input("Please enter password length: "))

password = "".join(random.sample(all_chars, length))

# Checking password complexity
if check_password_complexity(password):
    print("Generated password: ", password)
    print("The password meets the complexity requirements!")
else:
    print("Generated password: ", password)
    print("The password does NOT meet the complexity requirements.")
