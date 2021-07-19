# This program collects user input on rainfall
# for 12 months and then averages the total.

years = int(input('How many years do you want to track? '))
months = 12
total = 0.0

# Get user info on rainfall
for years_rain in range(years):
            print('Year Number', years_rain + 1)
            print('------------------------------')
for month in range(months):
    print('How many inches for month ', month + 1, end='')
    rain = int(input(' did it rain? '))
    total += rain

# Calculations
number_months = years * months
average = total / number_months

# Print results
print('The total inches of rainfall was ', format(total, '.2f'),'.')  
print('The number of months calculated was', number_months)
print('The average rainfall was', format(average, '.2f'), 'inches')
