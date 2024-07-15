import string
import random

def generate_password():
    characters_set = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters_set) for _ in range(10))
    return password

print("Do you want to generate a random 10-character password? (Y/N): ")
answer = input().upper()
if answer == "Y":
    print("Your generated password is:", generate_password())
else:
    print("Exiting the program.")