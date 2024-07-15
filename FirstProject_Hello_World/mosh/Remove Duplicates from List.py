# Initial list with duplicates
numbers = [1, 3, 2, 4, 5, 6, 2, 7, 4, 8, 1, 9, 1]

# Create a new list to store unique elements
unique_numbers = []

# Iterate through each number in the original list
for number in numbers:
    # Check if the number is already in the unique_numbers list
    if number not in unique_numbers:
        # If not, add it to the unique_numbers list
        unique_numbers.append(number)
unique_numbers.sort()

# Print the list without duplicates
print(unique_numbers)

