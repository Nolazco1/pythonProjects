# This program generates a random number
# in the range of 1-100 and asks the user
# what the number is.

import random

# Gets a random integer
num = random.randint(1, 100)

# Guess the number
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    guess = int(guess)
    if guess == num:
        print('You guess the correct number!')
    elif guess < num:
        print('Too low, try again.')
    elif guess > num:
        print('Too high, try again.')
