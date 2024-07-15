import random
hearts = 3

chars = "123456789"
random_number = random.choice(chars)
print(random_number)
while True:
    inpt = int(input("Guess the number"))
    if inpt == random_number:
        print("You won")
        break
    else:
        print("You got it wrong, try again ")
        hearts -= 1
    if hearts == 1:
        hint_lower = int(random_number) - 2
        hint_higher = int(random_number) + 2
        print(f"hint: The number is somewhere between {hint_lower} and {hint_higher}! ")
    if hearts == 0:
        print("You lost")
        break

