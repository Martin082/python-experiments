numbers = [1, 2, 3, 4, 5, 10, 99, 27]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)