
import random
word_list = ["ardvark", "baboon","camel"]

#Randomly chosing word
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for blank_s in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Guess letter: ").lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter  
print(display)




