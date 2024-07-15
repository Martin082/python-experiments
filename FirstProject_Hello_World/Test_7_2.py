import random

number = random.randint(1,10)

guess = input('Silly game, guess number from 1 to 10')
guess = int(guess)

if guess == number:
    print('You won')
else:
    print('You lost')




