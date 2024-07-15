# name = input("What's your name? ")
# age = input("How old are you? ")
# print("Hello " + name, "It's great that you are " + age, "years old
try:
    name = input("What's your name? ")
    while True:
        try:
            age = int(input("How old are you? "))
            break  # If the conversion is successful, exit the loop
        except ValueError:
            print("Please enter a valid number for your age.")
    print(f"Hello {name}, it's great that you are {age} years old!")
except Exception as e:
    print(f"An error occurred: {e}")


