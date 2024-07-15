vowel_list = "aeiou"
string = input("String: ").lower()
vowel_count = 0
for x in string:
    if x in vowel_list:
        vowel_count += 1

print(vowel_count)

