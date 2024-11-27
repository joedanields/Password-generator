import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    special = string.punctuation if include_special_chars else ''
    
    all_chars = lower + upper + digits + special
    

    password = []
    if include_uppercase:
        password.append(random.choice(upper))
    if include_numbers:
        password.append(random.choice(digits))
    if include_special_chars:
        password.append(random.choice(special))
    
    password += random.choices(all_chars, k=length - len(password))
    

    random.shuffle(password)
    
    return ''.join(password)


print("Welcome to the Password Generator!")
try:
    length = int(input("Enter the desired password length (minimum 4): "))
    if length < 4:
        print("Password length must be at least 4 to include all character types.")
    else:
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        # Generate the password
        password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
        print(f"Your generated password is: {password}")
except ValueError:
    print("Invalid input. Please enter numeric values for length.")
