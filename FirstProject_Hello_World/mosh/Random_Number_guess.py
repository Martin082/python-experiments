def char_game():
    hearts = 3
    number = 8
    while True:

        number_guess = int(input("Guess: "))
        if number_guess == number:
            print("you won")
            break
        else:
            hearts -= 1
            print(f"Wrong, you have {hearts} left")
            if hearts == 0:
                print("You lost")
                break


char_game()

