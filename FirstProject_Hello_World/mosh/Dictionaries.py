# You define a dictionary using curly braces {}

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])

# exercise
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""

number = input("Phone: ")
for ch in number:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# Here we do digits_mapping.get, because if the user enters a value that is not part of the dictionary,
# the program won't yell at them. it would retrieve "None" instead of a syntax error, otherwise we could do-
# print(digits_mapping[ch]

# Also, the (ch, "!"), the ! is the character that will be retrieved if the number the user inputs is not in the list.

# you can also do the code like this:
number = input("Phone: ")
for ch in number:
    if ch in digits_mapping:
        output += digits_mapping[ch] + " "
    else:
        output += "! "
print(output)