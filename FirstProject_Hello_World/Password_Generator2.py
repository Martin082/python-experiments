import random

print("password is ")

chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

password = ''

for x in range(16):
    password += random.choice(chars)

print(password)