count = 0
for number in range(0, 11):
    if number % 2 == 0:
        count += 1
        print(number, end="\t")
print()
print(f"We have {count} even numbers")