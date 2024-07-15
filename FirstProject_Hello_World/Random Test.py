# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# formatted = format(sum, ".2f")
# print(f"The result of this calculation is {formatted}")


while True:
    try:
        First_number = int(input("First number: "))
        break
    except ValueError:
        print("Please enter a numerical value, bro...")

while True:
    try:
        Second_number = int(input("Second number: "))
        break
    except ValueError:
        print("Please enter a numerical value, bro...")

Sum = First_number + Second_number
print(f'The result of your calculation is {Sum}')



# Another attempt at this code

import time
First = int(input("First: "))
Second = int(input("Second: "))
result = First + Second
time.sleep(3)
print(f"The result of your calculcation is {result}")
