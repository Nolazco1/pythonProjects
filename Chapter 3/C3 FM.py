# This program asks the user for a number 1-7
# and then displays the corresponding day of the week
# Mon = 1, Tues = 2, Wed = 3, Thurs = 4, Fri = 5
# Sat = 6, Sun = 7. Displays error if not within 1-7

day_of_week = input('What number of the week are you in? ')

# Shows corresponding day of the week

if day_of_week == '1':
    print('Monday')
elif day_of_week == '2':
    print('Tuesday')
elif day_of_week == '3':
    print('Wednesday')
elif day_of_week == '4':
    print('Thursday')
elif day_of_week == '5':
    print('Friday')
elif day_of_week == '6':
    print('Saturday')
elif day_of_week == '7':
    print('Sunday')
else:
    print('Error: Please choose between 1-7.')
