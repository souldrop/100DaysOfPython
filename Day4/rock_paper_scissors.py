# Rock Paper Scisissors
import random

Rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors!")
user_choice = input("Please choose one of the following: Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

computer_choice = random.randint(0, 2)
print(f"The computer has chosen: {computer_choice}")

