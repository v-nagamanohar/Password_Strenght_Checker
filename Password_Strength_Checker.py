import string
import random
import getpass

def check_password_strenght(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short (minimum 8 characters)")
    if not any(c.islower() for c in password): # any return true if anyone iterable is present in the given list
        issues.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digits")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing special character")
    return issues



def generate_strong_password(lenght=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    # random.choice(chars) returns the random chars from the given chars list 
    return "".join(random.choice(chars) for _ in range(lenght))


password = getpass.getpass("Enter a password: ") #  getpass doesn't relieve the password while typing

issues = check_password_strenght(password)
suggestion = generate_strong_password()

if not issues:
    print("Strong password! you are good to go")
else:
    print("You got weak password")
    for issue in issues:
        print(f"- {issue}")
    print("\n Suggesting you a strong password")
    print(suggestion)


