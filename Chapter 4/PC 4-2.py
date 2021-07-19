# This program determines if you will
# exceed your monthly budget.

budget = float(input('Enter your monthly budget: '))
expenses = 0
check = 0

# Expenses

while check >=0:
    check = float(input('Enter the expense amount or -1 to calculate: '))
    if check != -1:
        expenses += check

# Calculates budget expenses

balance = budget - expenses

if balance < 0:
    print("You haven't budgeted enough. You're going to be $", \
          format(-1 * balance, ',.2f'), ' short this month.', sep = '')
elif balance == 0:
    print("Watch out. You've budgeted just enough to make it through " +
          "the month.")
else:
    print('You will have $', format(balance, ',.2f'), ' extra this month.', \
          sep = '')
