weight = input("What's your weight? ")
weight_format = input("(L)bs or (K)g? ")
if weight_format.lower() == "lbs" or "l":
    weight_kg = int(weight) * 0.45359237
    float_weight_kg = round(weight_kg, 1)
    print(f"You weigh {float_weight_kg} kilograms, you fat fuck.")
elif weight_format.lower() == "kg" or "k":
    weight_lbs = int(weight) * 2.20462262
    float_weight_lbs = round(weight_lbs, 1)

    print(f"You weigh {float_weight_lbs} pounds, you fat fuck.")
