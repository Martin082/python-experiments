def edd_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("It's not even")


edd_odd(2)


def count_vowels(string):
    vowels = ["a", "e", "u", "y", "i", "o"]
    vowels_count = 0
    for ch in string:
        if ch in vowels:
            vowels_count += 1
    return vowels_count


string = input("Enter a string: ")
vowels_count = count_vowels(string)
print(vowels_count)
