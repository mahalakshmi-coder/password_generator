import random
import string

def generate_pwd(length=10,use_numbers =True,use_special_chars = True):

    letters = string.ascii_letters
    digits = string.digits if use_numbers else ''
    special_char = string.punctuation if use_special_chars else ''

    # Combine all character sets
    all_char = letters + digits + special_char

    if  not all_char:
        raise ValueError("No characters Available to generate password:")

    pwds = [random.choice(all_char) for i in range(length)]
    password = ''.join(pwds)
   
    return (password)

length = int(input("Enter the Length of the password you need:"))
use_numbers = input("Do you want to include Digits in your password(y/n)?").lower().strip() == "y"
use_special_chars = input("Do you want to include Special Characters in your password(y/n)?").lower().strip() == "y"

try:
    pwd = generate_pwd(length,use_numbers,use_special_chars)
    print(f"Generated password: {pwd}")
except ValueError as ve:
    print(f"Error: {ve}")

