message = input(">")
words = message.split()  # this method splits a string based on a value, in this case a space
# if you run this split method with a message "good morning cutie" it would retrieve:
# ['good', 'morning', 'cutie']
emojis = {
    ":)": "😂",
    ":(": "🙁",
    ":D": "😀"
}
output = ""
for word in words: # if here we do in message and not in words, every character will have a space after it
    # because below we have a space after every character, but the split method combines the characters in one
    output += emojis.get(word, word) + " " # you use the call method to extract the charcter if it is in the dictionary
    # (the first "word" after the emojis.get. if the word is not in the dictionary, you simply print the original word
print(output)

# Side Tip: you can split a string based on any character
sentence = "This is a string"
print(sentence.split())

print(sentence.split(maxsplit=1))
# The maxsplit optional parameter specifies how many maximum splits are allowed / possible, in this case 1


# hel
# uduehe
# hahaha