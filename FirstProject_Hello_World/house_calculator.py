def get_expected_costs(beds, baths):
    base_value = 80000
    cost_per_bed = 30000
    cost_per_bath = 10000
    expected_cost = base_value + (beds * cost_per_bed) + (baths * cost_per_bath)
    return expected_cost


option_one = get_expected_costs(2, 3)
option_two = get_expected_costs(3, 2)
option_three = get_expected_costs(3,3)
option_four = get_expected_costs (3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)



