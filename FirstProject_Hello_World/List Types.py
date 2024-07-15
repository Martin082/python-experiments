    # Strings in python are like real life objects (like a bycicle), they have certain capabilities.
numbers = [1,7,3,4,5]
numbers.append("hello")  # append means to add something in the end of something else
print(numbers)

print(numbers.count(5))    # This method counts the amount of times a specific value is present. in this case 5 is once

numbers.insert(3, 'lol') # you can also insert something with the index of where you want it
print(numbers)

numbers.remove('lol')  # You can remove stuff too
print(numbers)

print(1 in numbers)  # Boolian expression, returns either True or False. If there is '1' in 'numbers' it will say true

print(len(numbers))  # This function (len) will retrieve the number of elements in a list

print("juicy")

print(numbers.pop())        # This   method removes the last item in a list

print(numbers.index(5))    # This returns the index of the first occurrence of this item

numbers.sort()             # This sorts the numbers in ascending order
print(numbers)

numbers.reverse()          # This sorts the numbers in descending order
print(numbers)

numbers2 = numbers.copy()       # This creates a copy of the original list without modifying it. also, the copied list
numbers.append(10)              # is not connected directly to the original. as you can see we append 10 to the original
print(numbers2)                 # list but the copied list is not affected in any way


numbers.clear()  # This will remove everything from inside the list
print(numbers)


