numbers = range(5)
print(numbers)

numbers = range(5)
for x in numbers:
    if x == 0:
        continue
    print(x)

print('nice')

numbers = range(5, 10)
for number in numbers:
    print(number)

print('splendid')

numbers = range(5, 50, 5)
for x in numbers:
    print(x)

print('wonderful')
    # You don't have to store the range in a variable such as (numbers)
    # You can just call the range function whenever you need it. demonstration below

for number in range(5):
    print(number)