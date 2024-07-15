print(10 + 3)
print(10 / 3)
print(10 // 3)  # This is division but will return a whole number always
print(10 % 3)  # Returns the remainder of the division. 10/3, it goes 3 times (because 3x3 = 9) and you have 1 left over
print(10 ** 3)   # 10 на десета степен
x = 10
x += 3        # (the same as x = x +3)
3 != 4 # This means "Not equal"

x = 2.6
print(round(x))

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = int(weight / 0.45)
    print("Weight in lbs:" + str(converted))
elif unit.upper() == "L":
    converted = int(weight * 0.45)
    print("Weight in kg:" + str(converted))
