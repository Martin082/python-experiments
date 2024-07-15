numbers = [2, 2, 2, 2, 6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

for y in range(3):
    for x in range(1, 10):
        print(x, end=" ")
    print()  # This just prints a new line
    # By default, after every iteration of the loop, the new iteration will be printed on a new line, but if you set
    # the 'end =' with a comma, you can decide what you want to have after every iteration


# Small project for a rectangle
rows = int(input(" Rows: "))
columns = int(input("Columns "))
symbol = input("Symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
    # end = "" prevents from opening a new line after every symbol