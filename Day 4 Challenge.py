# Guess the secret number game in Python

name = input("Please enter your name: ")
print(f"Hi {name}, I have a challenge for you today.")
print("I have thought of a number between 1 and 100. And you get 8 tries to guess it.")

from random import *
num_guess = randint(1, 100)

tries = 8
while tries > 0:
    print(tries)
    number = int(input("Input the number: "))

    if number < 1 or number > 100:
        print('You have chosen a number that is not in the range. Please choose another one.')
        tries += -1
    elif number < num_guess:
        print('Oops, wrong answer. You chose a number smaller than the secret number.')
        tries += -1
    elif number > num_guess:
        print('Oops, wrong answer. You chose a number greater than the secret number')
        tries += -1
    else:
        print(f'Wohoo, you won! You were left with {tries} tries')
        break


if number != num_guess:
    print(f'Sorry, you lost :(. The correct answer was {num_guess}')
    exit
