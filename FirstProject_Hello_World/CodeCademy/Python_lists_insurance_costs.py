names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))

print(medical_records)
print()

num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records")

first_medical_record = medical_records[0]
print(f"Here is the first medical record: {first_medical_record}")

print()

medical_records.sort()
print(f"Here are the medical records sorted by insurance cost: {medical_records}")

print()

cheapest_three = medical_records[:3]
print(f'Here are the cheapest insurance costs in our medical records: {cheapest_three}')

print()

priciest_three = medical_records[-3:]
print(f'Here are the priciest insurance costs in our medical records: {priciest_three}')

print()

occurrences_paul = 0
for name in names:
  if name == "Paul":
    occurrences_paul += 1
  else:
   continue
print(occurrences_paul)


print()

new_medical_records = list(zip(names, insurance_costs))
new_medical_records.sort()
print(list(new_medical_records))

print()

middle_five_records = new_medical_records[3:7]
print(middle_five_records)