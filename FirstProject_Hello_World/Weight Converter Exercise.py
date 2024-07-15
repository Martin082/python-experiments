# My original code (it's wrong)
Weight = int(input("Weight "))
Weight_Format = input("(K)g or (L)bs: ")

if Weight_Format.lower() == "k" or "kg":
    print("You weigh", round(Weight * 2.2), "lbs")

elif Weight_Format == "L":
    print("You weigh", round(Weight // 2.2), "kg")

    # ChatGPT's code (Works, obviously)
Weight = int(input("Weight: "))
Weight_Format = input("(K)g or (L)bs: ")

if Weight_Format in ["K", "k", "kg", "KG"]:
    print("You weigh", round(Weight * 2.2), "lbs")
elif Weight_Format in ["L", "l", "lbs", "LBS"]:
    print("You weigh", round(Weight / 2.2), "kg")
else:
    print("Invalid weight format")

# Youtuber's code (Also works)
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(converted)
elif unit.upper() == "L":
    converted = weight * 0.45
    print(converted)
