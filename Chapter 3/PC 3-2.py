# This program asks a user to enter a person's
# age. The program will play indicating whether
# the person is infant, a teenager, or an adult.

age = float(input("What is the person's age? "))

# Determines age class

if age <= 1:
    print('This person is an infant.')
elif age <= 13:
    print('This person is a child.')
elif age <=20:
    print('This person is a teenager.')
elif age >= 20:
    print('This person is an adult.')

