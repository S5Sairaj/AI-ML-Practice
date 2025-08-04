import re

password = input("Enter your password: ")

length_error = len(password) < 8
uppercase_error = re.search(r"[A-Z]", password) is None
lowercase_error = re.search(r"[a-z]", password) is None
digit_error = re.search(r"[0-9]", password) is None
special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

if not (length_error or uppercase_error or lowercase_error or digit_error or special_error):
    print("Strong password.")
else:
    print("Weak password. Please ensure:")
    if length_error:
        print("- At least 8 characters")
    if uppercase_error:
        print("- At least one uppercase letter")
    if lowercase_error:
        print("- At least one lowercase letter")
    if digit_error:
        print("- At least one digit")
    if special_error:
        print("- At least one special character (!@#$%^&*(),.?\":{}|<>)")
