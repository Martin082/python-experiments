weight_lbs = int(input("What's your bodyweight in Pounds? "))
weight_kg = weight_lbs / 2.2046

if weight_kg.is_integer():
    # Convert weight_kg to integer if it's a whole number
    weight_kg_formatted = int(weight_kg)
else:
    # Round weight_kg to 1 decimal place if it has a fractional part
    weight_kg_formatted = round(weight_kg, 1)

print(f"You weigh {weight_kg_formatted} kilograms")


