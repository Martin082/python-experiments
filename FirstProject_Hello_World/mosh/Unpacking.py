coordinates = (1, 2, 3)  # Let's say we want to use these coordinates as values for different operations
# we would have to write smth like coordinates[0] * coordinates[1] * coordinates[2]... It's too long
# You can store the different values as separate values, as follows:
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
 # BUT
x, y, z = coordinates # This is called unpacking, and it's the same as what we have on line 4, 5, 6

# So you have:
coordinates = (1, 2, 3)
# If you will use the values in the tuple a lot, you can unpack them by doing:
x, y, z = coordinates

print(x)
print(y)
print(z)

# You can also unpack lists, not only tuples