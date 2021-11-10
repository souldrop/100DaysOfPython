# hangman game 
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess_word = input("Guess the word: ").lower()

if(guess_word == chosen_word):
    print("You guessed it right, you win!")
else:
    print("You guessed it wrong, you lose!")