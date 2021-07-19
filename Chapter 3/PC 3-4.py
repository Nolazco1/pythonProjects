# This program determines shipping charges
# based off the user input.

weight = float(input('Please enter the weight of the item in pounds: '))

# Shipping charges calculations

if weight <= 2:
    print('The shipping charge is $1.50 per pound.')
elif weight <= 6:
    print('The shipping charge is $3.00 per pound.')
elif weight <= 10:
    print('The shipping charge is $4.00 per pound.')
else:
    print('The shipping charge is $4.75 per pound.')
    

