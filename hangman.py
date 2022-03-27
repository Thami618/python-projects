
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

#Create blanks
#My loop will loop until everything is fiiled
end_of_game = False
while not end_of_game:
    guess = input("Guess letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position} \n Current letter: {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")



