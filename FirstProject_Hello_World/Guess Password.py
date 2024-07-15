import time

def main():
    correct_password = "0800"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = input("Please enter the password: ")
        if password == correct_password:
            print("Password is Correct")
            time.sleep(3)
            print("anna")
            return
        else:
            attempts += 1
            print("Wrong password")

    if attempts == max_attempts:
        print("You introduced a wrong password 3 times, you are blocked.")

if __name__ == "__main__":
    main()






