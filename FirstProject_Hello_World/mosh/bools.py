bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

print(bool_one)  # True--- Because it's true that 5 is not equal to 7
print(bool_two)  # False--- Because it's false that 1+1 is not equal to 2
print(bool_three)  # True--- Because it's true that 3 * 3 is equal to 9


# Or operator (if at least one of the arguments is True, then the entire bool is True
variable_one = True or (3 + 4 == 7)    # True because both are true
variable_two = (1 - 1 == 0) or False   # True because 1-1 == 0
variable_3 = (2 < 0) or True         # True because you have 2 True statemets
variable_4 = (3 == 8) or (3 > 4)     # False because neither of these is true


important = not True == False
important_2 = not False == True


# we add the not operator to the very beginning of the statement.
# not 1 + 1 == 2   (False)
# not 7 < 0        (True)

# Syntax for "not" statements:
# if not credits >= 120:  CORRECT SYNTAX
  # print("You do not have enough credits to graduate.")

# if credits not >= 120:      wrong SYNTAX
#   print("You do not have enough credits to graduate.")