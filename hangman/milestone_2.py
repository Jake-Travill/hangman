import random


word_list = ['apple', 'orange', 'banana', 'pineapple', 'mango']
word = random.choice(word_list)

guess = input("Please enter a letter: ").lower()
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That's not a valid input.")