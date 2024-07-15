import random

print('Your password:')

chars = "abcdefghijklmnopqrstuvwxyz!#@$%ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)



