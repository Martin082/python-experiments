# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

#In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

# Sal’s Shippers has several different options for a customer to ship their package:

# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.

# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.

# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.


weight = 4.8

# Ground Shipping
if weight <= 2:
  ground_shipping_cost = 20 + (1.50 * weight)
elif weight > 2 and weight <= 6:
  ground_shipping_cost = 20 + (3 * weight)
elif weight > 6 and weight <= 10:
  ground_shipping_cost = 20 + (4 * weight)
elif weight > 10:
  ground_shipping_cost = 20 + (4.75 * weight)
else:
  print("Error")
print(f"Cost of shipping by ground: {ground_shipping_cost} $")

# Ground Premium Shipping
premium_ground_shipping_cost = 125
print(f"Ground Shipping Premium: {premium_ground_shipping_cost} $")

# Drone Shipping
if weight <= 2:
  drone_shipping_cost = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_shipping_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_shipping_cost = weight * 12
elif weight > 10:
  drone_shipping_cost = weight * 14.25
drone_shipping_cost = round(drone_shipping_cost, 2)
print(f"Cost of shipping by drone: {drone_shipping_cost}", "$")
print()
# Determine the cheapest shipping option
cheapest_cost = min(ground_shipping_cost, premium_ground_shipping_cost, drone_shipping_cost)

if cheapest_cost == ground_shipping_cost:
    cheapest_option = "Ground Shipping"
elif cheapest_cost == premium_ground_shipping_cost:
    cheapest_option = "Premium Ground Shipping"
else:
    cheapest_option = "Drone Shipping"

print(f"The cheapest shipping option is {cheapest_option} with a cost of {cheapest_cost} $")
