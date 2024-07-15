while True:
    name = input("Please enter your name: ")

    if len(name) < 3:
        print("Error: The name has to be over 3 characters.")
    elif len(name) > 50:
        print("Error: The name can be a maximum of 50 characters.")
    else:
        print("Nice!")
        break
