# This program calculates Miles-Per-Gallon

miles = int(input('How many miles were driven? '))
gas = int(input('How much gas in gallons was used? '))

# Calculation

mpg = miles / gas

# Shows MPG

print('MPG =', format(mpg, '.2f'))
