# In math there is a thing called Matrix, a rectangulat array of numbers. basically like Excel
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][1])

# The first number (0) redirects the first list (1,2,3) and the second number (1) accesses the numbers within that list



# for each iteration of the below loop, it will run through the list, eg in the first iteration it goes through 1,2,3
  # on the second it goes through 4, 5, 6
for row in matrix:
    for item in row:
        print(item, end="\t")
print()


def flatten_2d_list(lst):
    return [item for sublist in lst for item in sublist]

# Example usage:
print(flatten_2d_list([[1, 2], [3, 4], [5, 6]]))  # Output: [1, 2, 3, 4, 5, 6]


drinks = ["coffee", "tea", "water"]
lunch = ["chicken", "pasta", "burger"]
dessert = ["cake", "chocolate"]

food = [drinks, lunch, dessert]

print(food[0][0])
# the first index [0] looks for the index of the list (drinks)
# The second index [0] looks for the index of the item within the drinks list (coffee)
