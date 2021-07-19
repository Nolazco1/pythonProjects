# This program prompts to user to enter a number
# range between 1-10. The program will display
# the corresponding number in Roman Numerals.

number = input('Please enter a number to convert: ')

# Roman Numeral converter

if number == '1':
    print('Roman Numeral: I')
elif number == '2':
    print('Roman Numeral: II')
elif number == '3':
    print('Roman Numeral: III')
elif number == '4':
    print('Roman Numeral: IV')
elif number == '5':
    print('Roman Numeral: V')
elif number == '6':
    print('Roman Numeral: VI')
elif number == '7':
    print('Roman Numeral: VII')
elif number == '8':
    print('Roman Numeral: VIII')
elif number == '9':
    print('Roman Numeral: IX')
elif number == '10':
    print('Roman Numeral: X')
else:
    print('Error: please enter a number between 1-10.')
