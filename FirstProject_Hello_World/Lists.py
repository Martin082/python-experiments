names = ['marto', 'John', "daniel", "johnny"]
print(names)
print(names[0])
    # If you want to print the first name from the list, use the index (0) in this case

print(names[-1])
    # You can use negative index for the list. -1 will retrieve the last name in the list.

print(names[-2])
    # This would retrieve the one to last names in the list

names[0] = "Martin"
print(names[0])
    # You can replace the value of a string in the list this way

print(names[0:3])
    # This will retrieve the names from the index, minus the last one

print(names[2:])
    # This will retrieve all the names from the list starting from the second one
