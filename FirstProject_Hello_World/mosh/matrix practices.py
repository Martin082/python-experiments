matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(len(matrix)) # This calculates the amount of rows the 2d list has


# How do i make this code so that it uses a nested loop to print first the index 0 of the first row, then on the second
# iteration to print the index 1 of the second row and so on?


chars = ["1", "2", "3"]
for num in chars:
    print(num + num, end="")
print()


def increment(numbers, by):
    incremented_value = numbers + by
    return incremented_value


number = int(input("What number do you want to increment? "))
number_to_increment_by = int(input("By how much do you want to increment? "))
result = increment(number, number_to_increment_by)
print(f"The result is {result}")
